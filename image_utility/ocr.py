import subprocess

from pytesseract import get_languages


class LanguageNotFoundError(Exception):
    pass


def install_tesseract(langs: list[str] = ["por"]):
    """
    Install Tesseract on Ubuntu

    langs - Languages to install for OCR (first 3 letters only).

    References:
        https://tesseract-ocr.github.io/tessdoc/Installation.html
    """

    try:
        subprocess.run("tesseract", stdout=subprocess.DEVNULL)

        for lang in langs:
            if lang not in get_languages():
                raise LanguageNotFoundError(f"Missing language: {lang}")
    except (FileNotFoundError, LanguageNotFoundError):
        args = [
            "sudo",
            "apt",
            "install",
            "-y",
            "tesseract-ocr",
            "libtesseract-dev",
        ]

        args.extend([f"tesseract-ocr-{lang}" for lang in langs])

        subprocess.run(args)
