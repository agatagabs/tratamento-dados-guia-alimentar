import re

def removeSetenceRepeat(text):
    arrayString = re.split(' |, |\n', text)
    
    for string in arrayString:
        numberOfRepeats = arrayString.count(string)
        if numberOfRepeats > 1:
            for _ in range(0, numberOfRepeats - 1):
                arrayString.remove(string)

    return arrayString
            
# file = open(file='Output.txt', mode='r', encoding='utf-8-sig')
# text = file.read()
# textFilter = removeSetenceRepeat(text)

# WordsRepeats = {}
# for string in textFilter:
#     repeats = textFilter.count(string)
#     if repeats > 1:
#         try:
#             WordsRepeats[string] = repeats
#         except:
#             pass

# print('\nWords Repeats:')

# for string in WordsRepeats:
#     print('{}: {}'.format(string, WordsRepeats[string])) 
