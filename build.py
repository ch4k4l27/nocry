import subprocess

def create_executable():
    # Defina o caminho para o arquivo principal e os dados a serem incluídos
    main_file = "scanner.py"
    additional_data = "utils/*:utils"

    # Construindo o comando
    command = [
        "pyinstaller",
        "--onefile",
        f"--add-data={additional_data}",
        main_file
    ]

    # Execute o comando
    print("Iniciando a criação do executável...")
    result = subprocess.run(command, capture_output=True, text=True)

    # Exibindo a saída
    if result.returncode == 0:
        print("Executável criado com sucesso!")
    else:
        print("Erro na criação do executável:")
        print(result.stderr)

if __name__ == "__main__":
    create_executable()
