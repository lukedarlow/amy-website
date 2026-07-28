from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def fit_without_crop(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = ImageOps.exif_transpose(image).convert("RGB")
    image.thumbnail(size, Image.Resampling.LANCZOS)
    return image


def main() -> None:
    mapping_path = Path(sys.argv[1])
    image_dir = Path(sys.argv[2])
    output_dir = Path(sys.argv[3])
    heic_dir = Path(sys.argv[4]) if len(sys.argv) > 4 else None
    output_dir.mkdir(parents=True, exist_ok=True)

    entries: list[tuple[str, str]] = []
    for line in mapping_path.read_text().splitlines():
        identifier, source = line.split("\t", maxsplit=1)
        entries.append((identifier, source))

    columns, rows = 5, 4
    cell_w, cell_h = 400, 420
    image_box = (370, 320)
    items_per_sheet = columns * rows
    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 14)

    for sheet_index in range(math.ceil(len(entries) / items_per_sheet)):
        sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "#efefeb")
        draw = ImageDraw.Draw(sheet)
        start = sheet_index * items_per_sheet
        page_entries = entries[start : start + items_per_sheet]

        for local_index, (identifier, source) in enumerate(page_entries):
            column = local_index % columns
            row = local_index // columns
            x, y = column * cell_w, row * cell_h
            draw.rounded_rectangle(
                (x + 5, y + 5, x + cell_w - 5, y + cell_h - 5),
                radius=8,
                fill="white",
            )

            source_path = Path(source)
            if heic_dir is not None:
                review_path = heic_dir / f"{source_path.name}.png"
            else:
                review_path = image_dir / f"{identifier}.jpg"
            image = fit_without_crop(Image.open(review_path), image_box)
            image_x = x + (cell_w - image.width) // 2
            image_y = y + 12 + (image_box[1] - image.height) // 2
            sheet.paste(image, (image_x, image_y))

            filename = Path(source).name
            label = f"{identifier}  {filename}"
            max_chars = 43
            lines = [label[i : i + max_chars] for i in range(0, len(label), max_chars)]
            text_y = y + 342
            for line in lines[:3]:
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                draw.text((x + (cell_w - text_width) // 2, text_y), line, fill="black", font=font)
                text_y += 19

        destination = output_dir / f"all-stills-{sheet_index + 1:02d}.jpg"
        sheet.save(destination, quality=91, optimize=True)
        print(destination)


if __name__ == "__main__":
    main()
