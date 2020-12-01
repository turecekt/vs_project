"""Input text or morse code .Output translated text or morse."""
from morse import MorseCodeTranslator

translator = MorseCodeTranslator()
# Insert text for translation to morse
text = "&@)(=!-+?"
# Insert morse for translation to text
morse = "-.. --- -... .-. -.--   -.. . -."

# Translate text to morse code
translated_morse = translator.translate_text(text)

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(translated_morse)
print(translated_text)
