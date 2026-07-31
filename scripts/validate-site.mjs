import { execFileSync } from 'node:child_process';
import { existsSync, lstatSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { extname, join, normalize, relative, resolve, sep } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const site = join(root, 'site');
const failures = [];

const fail = message => failures.push(message);
const walk = directory => readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
  const path = join(directory, entry.name);
  if (entry.isSymbolicLink()) {
    fail(`Deployment artifact must not contain a symbolic link: ${relative(root, path)}`);
    return [];
  }
  return entry.isDirectory() ? walk(path) : [path];
});

for (const required of ['index.html', 'styles.css', 'corrections.css', 'script.js']) {
  if (!existsSync(join(site, required))) fail(`Missing required file: site/${required}`);
}

let files = [];
if (existsSync(site) && lstatSync(site).isDirectory()) files = walk(site);

const portfolio = files.filter(path => relative(join(site, 'assets', 'portfolio'), path).split(sep).length === 1 && ['.jpg', '.jpeg', '.png', '.webp'].includes(extname(path).toLowerCase()));
if (portfolio.length !== 25) fail(`Expected 25 public portfolio images, found ${portfolio.length}`);

const artifactBytes = files.reduce((total, path) => total + statSync(path).size, 0);
const artifactLimit = 25 * 1024 * 1024;
if (artifactBytes > artifactLimit) fail(`Site artifact exceeds 25 MiB (${(artifactBytes / 1024 / 1024).toFixed(1)} MiB)`);

const htmlFiles = files.filter(path => extname(path).toLowerCase() === '.html');
for (const htmlFile of htmlFiles) {
  const html = readFileSync(htmlFile, 'utf8');
  const ids = new Set([...html.matchAll(/\bid=["']([^"']+)["']/g)].map(match => match[1]));
  const references = [...html.matchAll(/\b(?:href|src|data-src)=["']([^"']+)["']/g)].map(match => match[1]);

  for (const reference of references) {
    if (/^(?:https?:|mailto:|tel:|data:)/i.test(reference)) continue;
    if (reference.startsWith('/')) {
      fail(`${relative(root, htmlFile)} uses a root-relative URL: ${reference}`);
      continue;
    }
    if (reference.startsWith('#')) {
      if (reference.length > 1 && !ids.has(decodeURIComponent(reference.slice(1)))) {
        fail(`${relative(root, htmlFile)} links to missing fragment: ${reference}`);
      }
      continue;
    }

    const pathOnly = decodeURIComponent(reference.split(/[?#]/, 1)[0]);
    const target = resolve(join(htmlFile, '..'), normalize(pathOnly));
    if (target !== site && !target.startsWith(`${site}${sep}`)) {
      fail(`${relative(root, htmlFile)} references a path outside site/: ${reference}`);
    } else if (!existsSync(target)) {
      fail(`${relative(root, htmlFile)} references a missing file: ${reference}`);
    }
  }
}

try {
  execFileSync(process.execPath, ['--check', join(site, 'script.js')], { stdio: 'pipe' });
} catch (error) {
  fail(error.stderr?.toString().trim() || 'JavaScript syntax validation failed');
}

if (failures.length) {
  console.error(failures.map(message => `- ${message}`).join('\n'));
  process.exit(1);
}

console.log(`Validated ${files.length} public files, ${portfolio.length} portfolio images, and ${(artifactBytes / 1024 / 1024).toFixed(1)} MiB.`);
