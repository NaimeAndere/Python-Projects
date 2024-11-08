import py7zr
import os

def extract_all_7z(zip_dir):
    # Diretório onde os arquivos extraídos serão armazenados
    extract_dir = os.path.join(zip_dir, 'extracted_files')

    # Certifique-se de que o diretório de extração existe
    os.makedirs(extract_dir, exist_ok=True)

    # Lista todos os arquivos no diretório ZIP
    for filename in os.listdir(zip_dir):
        if filename.endswith('.7z'):
            zip_path = os.path.join(zip_dir, filename)
            with py7zr.SevenZipFile(zip_path, mode='r') as z:
                z.extractall(path=extract_dir)
            print(f'Extraído: {filename}')

# Chame a função com o caminho do diretório
