# QR Code Generator

A Tkinter desktop app that generates real, scannable QR codes from any text or URL — with a save-to-PNG option.

## Features

- Generates spec-compliant QR codes (proper encoding, error correction, and masking) using the `qrcode` library
- Live preview on a canvas inside the app
- Save the generated QR code as a PNG file anywhere on your machine
- Simple dark-themed UI

## Requirements

- Python 3.x
- `qrcode` and `Pillow` (for image generation and display)

Install dependencies:
```bash
pip install qrcode[pil]
```

## How to Run

```bash
python qr_code_generator.py
```

## Usage

1. Type any text or URL into the input field.
2. Click **GENERATE** to create the QR code — it's fully scannable with any phone camera or QR scanner app.
3. Click **SAVE** to export it as a PNG file.

## License

Free to use and modify.