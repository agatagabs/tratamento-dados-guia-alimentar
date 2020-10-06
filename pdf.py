from tika import parser
import re
from spellingCorrector import spellingCorrector
from separacaoFrases import separandoFrases
from removeWordRepeat import removeWordRepeat
from tirandoOsAcento import tirandoAcento
raw = parser.from_file(filename="guia_alimentar_populacao_brasileira_2ed.pdf", service='text')
raw = str(raw)

safe_text = raw.encode('utf-8-sig', errors='ignore').decode('ascii', 'ignore')

safe_text = str(raw).replace("\\", "").replace("\n", "\\n").replace('nnn', '').replace('nn', '').replace('n  ', '').replace("_", '').replace('lll', '')
safe_text = spellingCorrector(safe_text)
safe_list = separandoFrases(safe_text)
for frase in safe_list:
    print(frase)
    frase = removeWordRepeat(str(frase))
    frase = tirandoAcento(str(frase))

#print('--- safe text ---' )
#print(safe_text)
text_file = open("Output.txt", "w", encoding='utf-8-sig')

for item in safe_list:
    text_file.write("%s" % item)
text_file.close()