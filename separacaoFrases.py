def separandoFrases(texto):
    a = 0
    texto_separado = []
    for i in range(len(texto)):
        if(texto[i] == "!" or texto[i] == ";" or texto[i] == "." or texto[i] == "?"):
            texto_separado.append(texto[a:i] + " /n")
            a = i + 1
            
    return texto_separado

txt = "cachorro gato. pao com açucar? cao? gato? eu quero um cachroro e um gato; mas eu nao sei onde eu quero isso de verdade."

print(separandoFrases(txt))