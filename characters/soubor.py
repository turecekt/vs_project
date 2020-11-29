from os import path
import collections


soubor = input('Zadejte název dokumentu: ')
print(".............................................................")


# work with file
def fileExists(file):
    if(path.exists(file)):
        x = open(file, "r")
        print(x.read())
    else:
    	x = open(file, "w")
    	x.write(input("Napište text, který chcete mít v novém souboru: "))
    	x.close()


#insert text into variable
def varInsert(soubor):
    with open(soubor, "r") as file:
        txt = file.read().replace("\n", "")
    return txt


text = varInsert(soubor)
    

#number of characters
def charCount():
    celkem = 0
    for i in text:
        celkem += 1
    print("Počet znaků je ", celkem)
        

#counting most used char
def mostFreqChar():
    most = collections.Counter(text.lower()).most_common(1)[0]
    print("Nejpoužívanější znak je ", most)


#finding least used char
def leastFreqChar():
    all_freq = {}
    for i in text.lower():
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    least = min(all_freq, key = all_freq.get)
    print("Nejménně použitý znak je ", least)
    

# #alphabet average
# def aplhabetAvg():
#     for i in text:
#         if i in ""


fileExists(soubor)
varInsert(soubor)
print("-------------------------------------------------------------")
charCount()
mostFreqChar()
leastFreqChar()


input("\nKlávesou ENTER ukončíte program...")
