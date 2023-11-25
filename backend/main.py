import googletrans
from googletrans import Translator, LANGUAGES

translator = Translator()
# translated = translator.translate(text = 'Hola Mundo' )
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
# print(translated)

# print(translated.text)

def get_key(val):
   
    for key, value in googletrans.LANGUAGES.items():
        if val == value:
            return key
            print(key)
 
    return key

def translation(text, language):
    #translate to german
    translated = translator.translate(text, dest = get_key(language))
    detected_language = googletrans.LANGUAGES[translator.detect(text).lang]
    return translated.text, detected_language

# #detect the language
# print(translator.detect('Hola Mundo').lang)

# #available languages for translation
# print(googletrans.LANGUAGES)

