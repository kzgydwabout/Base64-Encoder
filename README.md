# Base64 Encoder (No `base64` Module)

This Python script encodes a string into Base64 without using the built-in `base64` module.

## Features

- Pure Python implementation
- No external dependencies
- Works with any UTF-8 string input

## Usage

### Command Line

```bash
python base64_encoder.py "Your string here"
```

### Interactive

```bash
python base64_encoder.py
# Then enter your string when prompted
```

## Example

```bash
$ python base64_encoder.py "hello"
aGVsbG8=
```

## How it Works

- The script converts the string to bytes.
- It processes the bytes in blocks of 3, encoding each block into 4 Base64 characters.
- Padding (`=`) is added if the input length is not a multiple of 3.

## License

MIT
