import unidecode

def tirandoAcento(frase):
    arrayString = frase.split()
    print(arrayString)
    for word in arrayString:
        if "/n" not in word: 
            word = unidecode.unidecode(word)
    
    return " ".join(arrayString)
