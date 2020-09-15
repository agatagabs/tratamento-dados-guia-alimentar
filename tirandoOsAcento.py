import unidecode

def tirandoAcento (texto):
    novoTexto = unidecode.unidecode(texto)
    return novoTexto
