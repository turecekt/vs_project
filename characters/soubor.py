from os import path
import collections


soubor = input("Zadejte název dokumentu. Pokud soubor neexistuje, vytvoří se nový: \n")


# work with file
def fileExists():
    if(path.exists(soubor)):
        x = open(soubor, "r")
        return x
    else:
    	x = open(soubor, "w")
    	x.write(input("Napište text, který chcete mít v novém souboru:\n\n"))
    	x.close()


#insert text into variable
def textIntoVar():
    with open(soubor, "r") as file:
        text = file.read().replace("\n", "")
    return text


#var with text
var = textIntoVar()


#number of characters
def charNum():
    celkem = 0
    for i in var:
        celkem += 1
    return celkem
        

#counting most used char
def mostFreq():
    most = collections.Counter(var.lower()).most_common(1)[0]
    return most


#finding least used char
def leastFreq():
    all_freq = {}
    for i in var.lower():
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    least = min(all_freq, key = all_freq.get)
    return least


#counting each char in text
def numOfEachChar():
    eachChar = {}
    for i in var.lower():
        if i in eachChar:
            eachChar[i] += 1
        else:
            eachChar[i] = 1
    return eachChar


#var of numEachChar
each = numOfEachChar()


#average
def average():
    pocetElements = len(each)
    return pocetElements
    

#method calling
fileExists()
charNum()
mostFreq()
leastFreq()
numOfEachChar()
average()       
     

print(fileExists().read())
print(".............................................")
print("Počet znaků je ", charNum())
print("Nejpoužívanější znak je ", mostFreq())
print("Nejménně použitý znak je ", leastFreq())
print("Počet každého obsaženého znaku v textu je ")
print(numOfEachChar())
print("Pruměrná četnost je ", charNum()/average())


input("\nKlávesou ENTER ukončíte program...")
