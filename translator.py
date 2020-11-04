#pip install googletrans
from spellchecker import SpellChecker
from googletrans import Translator
def traduzindo(text):
    translator = Translator()
    textSplit = SpellChecker().split_words(text)
    for word in textSplit:
        wordTranslated = translator.translate(word, dest='pt')
        text = text.replace(word, wordTranslated.text)
    return text 


