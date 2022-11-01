import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            print('Formato inválido', file=sys.stderr)
        with open(path_file, 'r') as file:
            data = file.read().splitlines()
            return data
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
