from pathlib import Path
import sys

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


TARGET_SIZE = (1152, 1800)
TARGET_ASPECT = TARGET_SIZE[0] / TARGET_SIZE[1]


def blend_patch(image: Image.Image, src_box: tuple[int, int, int, int], dst_box: tuple[int, int, int, int], feather: int = 16) -> None:
    patch = image.crop(src_box).resize((dst_box[2] - dst_box[0], dst_box[3] - dst_box[1]), Image.Resampling.LANCZOS)
    mask = Image.new("L", patch.size, 0)
    inner = Image.new("L", (max(1, patch.size[0] - feather * 2), max(1, patch.size[1] - feather * 2)), 255)
    mask.paste(inner, (feather, feather))
    mask = mask.filter(ImageFilter.GaussianBlur(radius=max(3, feather / 2)))
    image.paste(patch, dst_box, mask)


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: retouch_profile_photo.py input output")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    image = Image.open(input_path).convert("RGB")
    width, height = image.size

    crop_width = width
    crop_height = int(round(crop_width / TARGET_ASPECT))

    if crop_height > height:
        crop_height = height
        crop_width = int(round(crop_height * TARGET_ASPECT))

    left = int(round((width - crop_width) / 2))
    # Keep the portrait a touch wider so the face is not as tight in the frame,
    # while still trimming most of the extra sky.
    top = int(round(max(0, (height - crop_height) * 0.96)))
    crop_box = (
        left,
        top,
        left + crop_width,
        top + crop_height,
    )

    image = image.crop(crop_box).resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    blend_patch(image, (172, 1460, 238, 1588), (62, 1452, 128, 1580), feather=14)
    blend_patch(image, (128, 1608, 232, 1738), (18, 1602, 122, 1732), feather=18)
    blend_patch(image, (844, 1468, 944, 1666), (1028, 1462, 1128, 1660), feather=18)
    blend_patch(image, (878, 1368, 968, 1484), (1036, 1360, 1126, 1476), feather=16)

    image = ImageOps.autocontrast(image, cutoff=0.35)
    image = ImageEnhance.Color(image).enhance(1.04)
    image = ImageEnhance.Contrast(image).enhance(1.05)
    image = ImageEnhance.Sharpness(image).enhance(1.08)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, quality=94, subsampling=0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
