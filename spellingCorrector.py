#intall library pyspellchecker with pip install pyspellchecker

from spellchecker import SpellChecker

def spellingCorrector(text):
    spell = SpellChecker(language='pt')
    arrayString = spell.split_words(text)
    spellCorrect = []
    for word in arrayString:
        spellCorrect.append(spell.correction(word))
    return spellCorrect