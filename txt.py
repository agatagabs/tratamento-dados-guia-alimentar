import re
from spellingCorrector import spellingCorrector
from separacaoFrases import separandoFrases
from removeWordRepeat import removeWordRepeat
from tirandoOsAcento import tirandoAcento
from numerosPorExtenso import numerow
from transformOrdinalNumberInOrdinalText import transformOrdinalNumberInOrdinalText
#from translator import traduzindo

if __name__ == "__main__":
    ref_arquivo = open("pedaço.txt","r", encoding='utf-8')
    safetext = []
    for row in ref_arquivo:
        listafrase = row.split()
        if "/n" in listafrase:
            listafrase.remove("/n")
        frase = " ".join(listafrase)
        safetext.append(str(frase))
    safetext = " ".join(safetext)
    safetext = spellingCorrector(safetext)
    safe_list = separandoFrases(safetext)
    for frase in safe_list:
        frase = removeWordRepeat(str(frase))
        frase = numerow(str(frase))
        frase = transformOrdinalNumberInOrdinalText(str(frase))
        # frase = traduzindo(str(frase))
    text_file = open("outputdoTxt.txt", "w", encoding= "utf-8")

    for item in safe_list:
        text_file.write("%s" % item)
    text_file.close()