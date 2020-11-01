
from spellchecker import SpellChecker
import re 
spell = SpellChecker(language='pt')

def spellingCorrector(text):
    for word in text:
        string = text
        spell = SpellChecker(language='pt')
        arrayString = text.split()
        for word in arrayString:
            try:
                correcao = spell.correction(word)
                string = string.replace(word, correcao)
            except Exception as e:
                print('spelling corrector error:', e)
        return string
