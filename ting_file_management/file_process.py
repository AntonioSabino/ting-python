import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = {}
    lines_list = txt_importer(path_file)
    if instance:
        last_file = instance.search(len(instance)-1)
        if last_file['nome_do_arquivo'] == path_file:
            return
    data['nome_do_arquivo'] = path_file
    data['qtd_linhas'] = len(lines_list)
    data['linhas_do_arquivo'] = lines_list
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if not instance:
        return print('Não há elementos', file=sys.stdout)
    else:
        deleted = instance.dequeue()
        print(
            f'Arquivo {deleted["nome_do_arquivo"]} removido com sucesso',
            file=sys.stdout
        )


def file_metadata(instance, position):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
