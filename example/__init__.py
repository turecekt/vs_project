"""This is the "example" module.

The example module supplies one function, compute().  For example,

>>> compute(3)
3
"""


def compute(x):
    """Functon compute returns evaluation of expression using argument x.

    Args:
        - x - Input of the function

    Returns:
        - output - Output of the function
    """
    return x * x - 2 * x


soubor = open('basnicka.txt', encoding='utf-8')
obsah = soubor.read()
soubor.close()
"""print("kolikátý je to znak: ",obsah.find("#"))"""
ukoncovaciZnak = obsah.find("#")
obsah = obsah[0:ukoncovaciZnak]
print ("ukončovací znak: ",ukoncovaciZnak)
print(obsah)

"""str = input ("Enter a string")"""
str = obsah
print ("String is ",str)
str = str.lower()
str = str.replace(" ","")
print ("String is ",str)
count = {}
for x in str:
    if x in count.keys():
        count[x] +=1
         
    else:
        count[x] = 1
print(count)

for x in count.keys ():
    print("znak",x ,"se v textu vyskytuje: ",count[x])

print("Počet různých znaků: ",len(count))

MaxDictVal = max(count, key=count.get)
print("Nejčetnější znak:",MaxDictVal)

MinDictVal = min(count, key=count.get)
print("Nejméně četný znak:",MinDictVal)





"""Ještě pořešit:
    - jak vypsat všechny nejméně četné znaky
    - když text nebude obsahovat #, tak neodečítat -1
    - průměrná četnost"""





