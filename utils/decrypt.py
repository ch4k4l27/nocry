import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(encrypted_file_path, key):
    """Descriptografa o arquivo criptografado e salva o arquivo original."""
    with open(encrypted_file_path, "rb") as f:
        iv = f.read(16)   
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    decrypted_file_path = encrypted_file_path.replace(".enc", "")
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)

    print(f"Arquivo descriptografado: {decrypted_file_path}")
    os.remove(encrypted_file_path)
    return decrypted_file_path


def scan_and_decrypt(directory, key):
    """Escaneia o diretório e descriptografa os arquivos criptografados."""
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".enc"):
                file_path = os.path.join(root, file)
                try:
                    print(f"Descriptografando arquivo: {file_path}")
                    decrypt_file(file_path, key)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
