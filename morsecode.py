#Překladač textu do morseova kodu

# Abeceda pro překlad textu do morse 
def tomorse():
    abeceda = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
           "k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
           "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
               
    return abeceda

abeceda = tomorse()
# Vstup pro zadání textu
text = input("Zadej text který chceš přenést do morseovky : ")

morse_code = ""

for pismeno in text:
    if pismeno.lower() in abeceda.keys():
        morse_code += abeceda[pismeno.lower()] + " "
    else:
        morse_code += pismeno.lower() + " "
        
# Výstup překladače    
print(morse_code)
