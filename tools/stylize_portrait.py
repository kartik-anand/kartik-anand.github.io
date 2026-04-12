from pathlib import Path
import sys

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageOps


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: stylize_portrait.py input output")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    image = Image.open(input_path).convert("RGB")
    width, height = image.size

    target_aspect = 0.88
    crop_width = width
    crop_height = int(round(crop_width / target_aspect))

    if crop_height > height:
        crop_height = height
        crop_width = int(round(crop_height * target_aspect))

    left = (width - crop_width) / 2
    top = max(0, (height - crop_height) * 0.18)
    crop_box = (
        int(round(left)),
        int(round(top)),
        int(round(left + crop_width)),
        int(round(top + crop_height)),
    )

    image = image.crop(crop_box).resize((960, 1090), Image.Resampling.LANCZOS)

    base = image.filter(ImageFilter.MedianFilter(size=3))
    base = base.filter(ImageFilter.SMOOTH_MORE)
    poster = ImageOps.posterize(base, 5)

    edges = image.convert("L").filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.invert(edges)
    edges = ImageOps.autocontrast(edges)
    edges = ImageEnhance.Contrast(edges).enhance(1.35)
    edges = edges.point(lambda value: 255 if value > 206 else int(value * 0.78))
    edge_layer = Image.merge("RGB", (edges, edges, edges))

    inked = ImageChops.multiply(poster, edge_layer)
    stylized = Image.blend(poster, inked, 0.38)
    stylized = stylized.filter(ImageFilter.SMOOTH)
    stylized = ImageEnhance.Sharpness(stylized).enhance(1.18)
    stylized = ImageEnhance.Color(stylized).enhance(0.94)
    stylized = ImageEnhance.Contrast(stylized).enhance(1.05)

    cool_wash = Image.new("RGB", stylized.size, (238, 244, 249))
    stylized = Image.blend(stylized, cool_wash, 0.05)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    stylized.save(output_path, format="PNG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
