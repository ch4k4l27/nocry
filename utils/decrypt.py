import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from tqdm import tqdm
import time

def decrypt_file(encrypted_file_path, key):
    """Descriptografa o arquivo criptografado e salva o arquivo original."""
    try:
        if os.path.getsize(encrypted_file_path) < 16:  # Arquivo muito pequeno para ser criptografado corretamente
            print(f"Arquivo muito pequeno para descriptografar: {encrypted_file_path}")
            return None

        with open(encrypted_file_path, "rb") as f:
            iv = f.read(16)   
            encrypted_data = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        decrypted_file_path = encrypted_file_path.replace(".enc", "")
        with open(decrypted_file_path, "wb") as f:
            f.write(decrypted_data)

        print(f"Decrypt: {decrypted_file_path}")
        os.remove(encrypted_file_path)
        return decrypted_file_path
    except ValueError as e:
        print(f"Erro ao descriptografar o arquivo {encrypted_file_path}: {e}")
        return None

def scan_and_decrypt(directory, key):
    """Escaneia o diretório e descriptografa os arquivos criptografados."""
    files_to_decrypt = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".enc"):
                files_to_decrypt.append(os.path.join(root, file))

    for file_path in tqdm(files_to_decrypt, desc="Descriptografando arquivos", unit="arquivo"):
        decrypt_file(file_path, key)
        time.sleep(0.1)
