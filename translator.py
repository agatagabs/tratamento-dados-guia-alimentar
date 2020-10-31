#pip install googletrans
from googletrans import Translator
import spellchecker
def traduzindo(text):
    translator = Translator()
    spell = SpellChecker()
    textSplit = spell.split_words(text)
    for word in textSplit:
        wordTranslated = translator.translate(word, dest='pt')
        text = text.replace(word, wordTranslated.text)
    return text
