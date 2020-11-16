import os

def removeNumbersTogether(filename):
    try:
        os.remove("result.txt")
    except:
        pass
    fileInput = open(file=filename, encoding='utf-8')
    fileOutput = open("result.txt", encoding='utf-8', mode='a')
    SeaOfPhrases = fileInput.read().split('\n')
    # count = 0
    for phrase in SeaOfPhrases:
        SeaOfStrings = phrase.split()
        for string in SeaOfStrings:
            numeros = [
            'zero' in string,
            'um' in string,
            'dois' in string,
            'tres' in string,
            'quatro' in string,
            'cinco' in string,
            'seis' in string,
            'sete' in string,
            'oito' in string,
            'nove' in string
            ]
            if numeros.count(True) > 1:
                SeaOfStrings.remove(string)
                # count += 1
        fileOutput.writelines((" ".join(SeaOfStrings)) + '\n')
    fileInput.close()
    fileOutput.close()
    # print(count)
            