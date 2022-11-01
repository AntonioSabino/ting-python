import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = {}
    lines_list = txt_importer(path_file)
    if instance:
        last_file = instance.search(len(instance)-1)
        if last_file["nome_do_arquivo"] == path_file:
            return
    data["nome_do_arquivo"] = path_file
    data["qtd_linhas"] = len(lines_list)
    data["linhas_do_arquivo"] = lines_list
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
