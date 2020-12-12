from morse import MorseCodeTranslator

translator = MorseCodeTranslator()

text = "Testovaci string na preklad do morseovky a zpet."

# Translate text to morse code
morse = translator.translate_text(text)

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(morse)
print(translated_text)
