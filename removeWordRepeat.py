from spellchecker import SpellChecker

def removeWordRepeat(text):
    spell = SpellChecker(language='pt')
    arrayString = spell.split_words(text)
    for string in arrayString:
        numberOfRepeats = arrayString.count(string)
        if numberOfRepeats > 1:
            for _ in range(0, numberOfRepeats - 1):
                arrayString.remove(string)

    for string in arrayString:
        numberOfRepeats = arrayString.count(string)
        if numberOfRepeats > 1:
            for _ in range(0, numberOfRepeats - 1):
                arrayString.remove(string)

    return arrayString