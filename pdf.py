from tika import parser

raw = parser.from_file("guia_alimentar_populacao_brasileira_2ed.pdf")
print(raw.__dict__)
raw = str(raw)

safe_text = raw.encode('utf-8-sig', errors='ignore').decode('ascii', 'ignore')

safe_text = str(raw).replace("\\", "").replace("\n", "\\n")
#print('--- safe text ---' )
#print(safe_text)
print(type(safe_text))
text_file = open("Output.txt", "w", encoding='utf-8-sig')
text_file.write(safe_text)
text_file.close()