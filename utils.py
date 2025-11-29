import os

def get_stored_key():
    try:
        with open("key.txt", "r") as f:
            return f.read().strip()
    except:
        return None

def xor_engine(text, key):
    result = []
    key_len = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_len]
        res = ord(char) ^ ord(key_char)
        result.append(chr(res))
    return "".join(result)

def encrypt_hex(data, key):
    str_data = str(data)
    raw = xor_engine(str_data, key)
    return raw.encode('latin-1').hex()

def decrypt_hex(hex_data, key):
    try:
        raw = bytes.fromhex(hex_data).decode('latin-1')
        return xor_engine(raw, key)
    except:
        return "Error"