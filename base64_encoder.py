import sys

BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode_base64(input_string):
    # Convert input string to bytes
    byte_array = bytearray(input_string, "utf-8")
    encoded = ""
    # Process input in blocks of 3 bytes
    for i in range(0, len(byte_array), 3):
        block = byte_array[i:i+3]
        # Pad block if less than 3 bytes
        padding = 3 - len(block)
        block += b'\x00' * padding
        # Combine block into a single integer
        block_int = (block[0] << 16) + (block[1] << 8) + block[2]
        # Extract 6-bit segments and map to Base64 characters
        for j in range(18, -1, -6):
            index = (block_int >> j) & 0x3F
            encoded += BASE64_ALPHABET[index]
        # Add padding if needed
        if padding:
            encoded = encoded[:-padding] + "=" * padding
    return encoded

if __name__ == "__main__":
    if len(sys.argv) > 1:
        to_encode = sys.argv[1]
    else:
        to_encode = input("Enter string to encode: ")
    print(encode_base64(to_encode))
