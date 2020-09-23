import re

def removeSetenceRepeat(text):
    arrayString = re.split(' |, |\n|. |; |: ', text)
    
    for string in arrayString:
        numberOfRepeats = arrayString.count(string)
        if numberOfRepeats > 1:
            for _ in range(0, numberOfRepeats - 1):
                arrayString.remove(string)

    return arrayString