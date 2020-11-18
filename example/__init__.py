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
x=2
print(x**2)
print (compute(1))
print("___")

retezec = "Abeceda"
print(retezec.lower())
retezecMalym = retezec.lower()
print(retezec.count("a"))
print(retezecMalym.count("a"))
print(retezecMalym.count("b"))
a = retezecMalym.count("a")
b = retezecMalym.count("b")
nejcetnejsi = print(max(a,b))
text = "Ananas"
def pocetZnaku(text):

    return text.count("a")
print("počet znaků")
print(pocetZnaku(text))


str = input ("Enter a string")
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
    - Text se bude načítat ze souboru
    - průměrná četnost"""




