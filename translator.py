#pip install googletrans
from googletrans import Translator
def traduzindo(text):
    translator = Translator()
    for word in text: 
        lingua = translator.detect(word)
        if lingua == "en":
            translator.translate(word)
    return text        

