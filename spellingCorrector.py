from spellchecker import SpellChecker
import re

def spellingCorrector(text):
    spell = SpellChecker()
    arrayString = re.split(' |, |\n|. |; |: ', text)
    arrayString = spell.unknown(arrayString)
    spellCorrect = []
    for word in arrayString:
        spellCorrect.append(spell.correction(word))
    return spellCorrect

open('batata.txt', 'w').write(spellingCorrector(open('Output.txt').read()))