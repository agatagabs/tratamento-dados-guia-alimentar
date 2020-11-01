def numerow(texto):
    dic_Numeros = {'0': 'zero', '1': 'um', '2': 'dois', '3': 'três', '4': 'quatro','5': 'cinco', '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove'}
    for letter in texto:
        if letter in dic_Numeros.keys():
            print(dic_Numeros[letter])
            texto = texto.replace(letter,dic_Numeros[letter])
    return texto