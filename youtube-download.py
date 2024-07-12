import os
import argparse
from pytube import YouTube
from tqdm import tqdm

def on_progress(stream, chunk, bytes_remaining):
    global pbar
    # Calcula o progresso atual
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pbar.update(len(chunk))

def download_youtube_video(url, output_path):
  try:
    # Cria um objeto YouTube com a URL do vídeo
    yt = YouTube(url, on_progress_callback=on_progress)

    # Seleciona a stream de maior resolução disponível
    stream = yt.streams.get_highest_resolution() 

    # Inicializa a barra de progresso
    global pbar
    pbar = tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=yt.title)

    # Faz o download do vídeo
    stream.download(output_path=output_path)
    pbar.close()
    print("\033[92mDownload concluído!\033[0m")

  except Exception as e:
    print("\033[91mOcorreu um erro: {}\033[0m".format(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download de vídeos do YouTube.')
    parser.add_argument('video_url', type=str, help='URL do vídeo do YouTube que você quer baixar')
    parser.add_argument('--output_path', type=str, default='./videos', help='Caminho onde o vídeo será salvo')
    
    args = parser.parse_args()
    download_youtube_video(args.video_url, args.output_path)