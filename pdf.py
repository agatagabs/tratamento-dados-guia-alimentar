from tika import parser

<<<<<<< HEAD
raw = parser.from_file("guia_alimentar_populacao_brasileira_2ed.pdf")
print(raw.__dict__)
=======
raw = parser.from_file(filename="guia_alimentar_populacao_brasileira_2ed.pdf", service='text')
>>>>>>> 82d40541d253280bc5789610e1d104ce3503e518
raw = str(raw)

safe_text = raw.encode('utf-8-sig', errors='ignore').decode('ascii', 'ignore')

safe_text = str(raw).replace("\\", "").replace("\n", "\\n")
#print('--- safe text ---' )
#print(safe_text)
print(type(safe_text))
text_file = open("Output.txt", "w", encoding='utf-8-sig')
text_file.write(safe_text)
text_file.close()