

def convert(input_number):
    x = input_number
    k = []
    
    while (input_number > 0):
        # input_number/8-->%(vratí zbytek)
        a = int(float(input_number % 8))

        # (a) připojíme k poli
        k.append(a)

        # prvek input_number/a(zbytek) a to cele/8
        input_number = (input_number - a) / 8

        # načte pole
        text = ""

    # proces kdy se pole otočí
    for j in k[::-1]:
        text = text + str(j)

    return(text)

