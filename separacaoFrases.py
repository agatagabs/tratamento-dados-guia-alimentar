def separandoFrases(texto):
    a = 0
    texto_separado = []
    for i in range(len(texto)):
        if(texto[i] == "!" or texto[i] == ";" or texto[i] == "." or texto[i] == "?"):
            s = (texto[a:i] + " \n").lstrip().capitalize()
            texto_separado.append(s)
            a = i + 1
            
    return texto_separado


