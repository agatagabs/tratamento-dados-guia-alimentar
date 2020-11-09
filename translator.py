#pip install googletrans
from spellchecker import SpellChecker
from google.cloud import translate_v2 as translate

def traduzindo(text):
    translator = translate.Client()
    textSplit = SpellChecker().split_words(text)
    for word in textSplit:
        if translator.detect_language(word)["language"] == 'en':
            wordTranslated = translator.translate(word, target_language='pt')
            text = text.replace(word, wordTranslated["translatedText"])
    return text 