# YouTube Video Downloader

Este é um script Python para baixar vídeos do YouTube, utilizando as bibliotecas `pytube` e `tqdm`.

## Requisitos

- Python 3.6 ou superior
- `pytube`
- `tqdm`

## Instalação

### 1. Instalar o Python

Se você ainda não tem o Python instalado, você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/downloads/).

### 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)

Criar um ambiente virtual é uma boa prática para gerenciar dependências. Para criar e ativar um ambiente virtual, execute os seguintes comandos no terminal ou prompt de comando dentro do diretório onde quer iniciar o script:

```sh
# Cria um ambiente virtual chamado 'env'
python -m venv env

# Ativa o ambiente virtual
# No Windows
env\Scripts\activate

# No macOS/Linux
source env/bin/activate
``` 

### 3. Instalar as Dependências
```sh 
pip install pytube tqdm
```

## Sintaxe 
`python youtube-download.py <url> [--output_path <output_path>]`

- `<url>`: URL do vídeo do YouTube que você quer baixar.
- [--output_path `<output_path>`]: (Opcional) Caminho onde o vídeo será salvo. O padrão é ./videos.

### Exemplos de Execução
```sh
python youtube-download.py https://www.youtube.com/abc 
```

```sh
python youtube-download.py https://www.youtube.com/abc  --output_path ./CustomFolder
```

