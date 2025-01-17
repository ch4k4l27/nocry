import os
import sys

def get_key():
    """Detecta se há um ambiente gráfico disponível e solicita a chave de forma apropriada."""
    # Verifica se está no Windows ou se a variável DISPLAY está definida
    if os.name == 'nt' or os.environ.get('DISPLAY'):
        try:
            # Tenta usar a interface gráfica
            import tkinter as tk
            from tkinter import simpledialog

            root = tk.Tk()
            root.withdraw()  # Oculta a janela principal
            key = simpledialog.askstring("Descriptografia", "Digite a chave para descriptografar os arquivos:")
            if key is None:
                print("Nenhuma chave fornecida. A operação foi cancelada.")
                sys.exit(1)
            return key
        except Exception as e:
            print(f"Erro ao inicializar a interface gráfica: {e}")
            print("Mudando para entrada via terminal.")
    
    # Caso não tenha ambiente gráfico, usa o terminal
    return input("Digite a chave para descriptografar os arquivos: ")
