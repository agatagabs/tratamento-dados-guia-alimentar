def removeSetenceRepeat(text):
    arrayString = text.split()
    
    for string in arrayString:
        numberOfRepeats = arrayString.count(string)
        if numberOfRepeats > 1:
            for _ in range(0, numberOfRepeats - 1):
                arrayString.remove(string)

    return arrayString
            
# text = 'Batata Batata Batata Batata'
# print(removeSetenceRepeat(text))