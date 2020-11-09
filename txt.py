from tika import parser
import re
from spellingCorrector import spellingCorrector
from separacaoFrases import separandoFrases
from removeWordRepeat import removeWordRepeat
from tirandoOsAcento import tirandoAcento
from numerosPorExtenso import numerow
from transformOrdinalNumberInOrdinalText import transformOrdinalNumberInOrdinalText
from translator import traduzindo

if __name__ == "__main__":
    f = "output-2.txt"
    safe_text = open(f, 'rb').read()
    print(str(safe_text.encode('utf-8')))
    #safe_text = raw.encode('utf-8-sig', errors='ignore').decode('ascii', 'ignore')

    safe_text = str(safe_text)
    safe_text = spellingCorrector(safe_text)
    safe_list = separandoFrases(safe_text)
    for frase in safe_list:
        print(frase)
        frase = removeWordRepeat(str(frase))
        frase = numerow(str(frase))
        frase = transformOrdinalNumberInOrdinalText(str(frase))
        frase = tirandoAcento(str(frase))
        frase = frase.lstrip().replace("\\", "").replace("\n", "\\n").replace('nnn', '').replace('nn', '').replace('n  ', '').replace("_", '').replace('lll', '').capitalize()

    #print('--- safe text ---' )
    #print(safe_text)
    text_file = open("output1.txt", "w")

    for item in safe_list:
        text_file.write("%s" % item)
    text_file.close()