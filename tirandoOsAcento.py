import unidecode

def tirandoAcento(texto):
    for word in texto:
        novoTexto = unidecode.unidecode(word)
        return novoTexto
