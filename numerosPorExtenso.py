def numerow(texto):
    dic_Numeros = {'0': 'zero', '1': 'um', '2': 'dois', '3': 'três', '4': 'quatro','5': 'cinco', '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove'}
    texto = texto.split()    
    for item in texto:
        word = []     
        for letter in item:
            if letter in dic_Numeros:
                word.append(dic_Numeros[letter])
            else:
                word.append(letter)
        word1 = "".join(word)
        texto[texto.index(item)] = word1
    texto = " ".join(texto)
    return texto
