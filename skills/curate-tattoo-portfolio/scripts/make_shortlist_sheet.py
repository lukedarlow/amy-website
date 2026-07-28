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
    manifest = Path(sys.argv[1])
    review_dir = Path(sys.argv[2])
    destination = Path(sys.argv[3])
    title = sys.argv[4]
    entries = [line.split("\t", 2) for line in manifest.read_text().splitlines()]

    columns = 5
    rows = math.ceil(len(entries) / columns)
    cell_w, cell_h = 400, 430
    header_h = 80
    sheet = Image.new("RGB", (columns * cell_w, header_h + rows * cell_h), "#efefeb")
    draw = ImageDraw.Draw(sheet)
    title_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 28)
    label_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 13)
    draw.text((22, 22), title, fill="black", font=title_font)

    for index, (rank, identifier, source) in enumerate(entries):
        column, row = index % columns, index // columns
        x, y = column * cell_w, header_h + row * cell_h
        draw.rounded_rectangle(
            (x + 5, y + 5, x + cell_w - 5, y + cell_h - 5),
            radius=8,
            fill="white",
        )
        filename = Path(source).name
        image = fit_without_crop(Image.open(review_dir / f"{filename}.png"), (370, 320))
        image_x = x + (cell_w - image.width) // 2
        image_y = y + 12 + (320 - image.height) // 2
        sheet.paste(image, (image_x, image_y))

        label = f"#{rank}  {filename}"
        max_chars = 43
        lines = [label[i : i + max_chars] for i in range(0, len(label), max_chars)]
        text_y = y + 348
        for line in lines[:3]:
            bbox = draw.textbbox((0, 0), line, font=label_font)
            width = bbox[2] - bbox[0]
            draw.text((x + (cell_w - width) // 2, text_y), line, fill="black", font=label_font)
            text_y += 19

    destination.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(destination, quality=92, optimize=True)
    print(destination)


if __name__ == "__main__":
    main()
