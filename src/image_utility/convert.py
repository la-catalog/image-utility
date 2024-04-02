from io import BytesIO

from PIL import Image


def try_convert(
    img_bytes: bytes,
    formats: list[str],
) -> tuple[bytes | None, str | None]:
    """
    Try to convert an image to any of the formats given.

    img_bytes - Image bytes
    formats - File formats to try converting to (sorted by priority)
    """

    for format in formats:
        if new_img := convert(img_bytes, format, error=False):
            return new_img, format
    return None, None


def convert(img_bytes: bytes, format: str, error: bool = True) -> bytes | None:
    """
    Convert an image to an specific format.

    img_bytes - Image bytes
    format - File format to be converted to
    error - Whenever should raise error on failing converting (otherwise return None)
    """

    try:
        old_img = BytesIO(img_bytes)
        new_img = BytesIO()

        Image.open(old_img).save(new_img, format)

        return new_img.getvalue()
    except:
        if error:
            raise
    return None
