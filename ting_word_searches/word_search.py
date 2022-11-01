def exists_word(word, instance):
    data = []
    for i in range(len(instance)):
        occurrences = []
        file = instance.search(i)
        for line, content in enumerate(file['linhas_do_arquivo']):
            if word.lower() in content.lower():
                occurrences.append({"linha": line + 1})
        if occurrences:
            data.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
