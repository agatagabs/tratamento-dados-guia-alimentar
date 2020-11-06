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
    #f = "guia_alimentar_populacao_brasileira_2ed.pdf"
    f="capitulo1.pdf"
    raw = parser.from_file(filename=f, service='text')
    raw = str(raw)
    safe_text = raw
    #safe_text = raw.encode('utf-8-sig', errors='ignore').decode('ascii', 'ignore')

    safe_text = str(safe_text).replace("\\", "").replace("\n", "\\n").replace('nnn', '').replace('nn', '').replace('n  ', '').replace("_", '').replace('lll', '')
    safe_text = spellingCorrector(safe_text)
    safe_list = separandoFrases(safe_text)
    for frase in safe_list:
        frase = removeWordRepeat(str(frase))
        frase = numerow(str(frase))
        frase = transformOrdinalNumberInOrdinalText(str(frase))
        frase = tirandoAcento(str(frase))

    #print('--- safe text ---' )
    #print(safe_text)
    text_file = open("output1.txt", "w", encoding='utf-8-sig')

    for item in safe_list:
        text_file.write("%s" % item)
    text_file.close()