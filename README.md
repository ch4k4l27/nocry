# Sistema de Criptografia e Descriptografia de Arquivos

Este é um sistema simples para criptografar e descriptografar arquivos recursivamente em um diretório, utilizando a biblioteca `cryptography` para a segurança dos dados. O projeto também inclui uma barra de progresso com `tqdm` para melhorar a experiência do usuário.

## Funcionalidades

- Criptografar todos os arquivos em um diretório (exceto os já criptografados).
- Descriptografar todos os arquivos criptografados em um diretório.
- Interface de texto com barra de progresso.
- Detecção automática de arquivos já processados.

## Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em seu sistema.

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/sistema-criptografia.git
    cd sistema-criptografia
    ```

2. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```

3. Execute
    ```bash
        python scanner.py 
        #or
        python3 scanner.py
    ```
## Gerando instaldor
> vai de acordo com o sistema que vc rodar
> lembre-se de instalar pyinstaller
    ```bash
        pyinstaller.exe --onefile --noconsole --add-data "utils/*:utils" .\scanner.py
    ```
