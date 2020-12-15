def vypocti_delitelov(cislo):
    pocet_delitelov=0
    if cislo>10:
        pocet_delitelov=1
    for i in range(1,10):
        if cislo%i==0:
              pocet_delitelov=pocet_delitelov+1
    return pocet_delitelov

def je_prvocislo(cislo):
    pocet_delitelov =  vypocti_delitelov(cislo)
    if cislo<0:
       return None
    elif pocet_delitelov==2:
       return True
    elif pocet_delitelov!=2:
       return False
            
       

def popis(cislo):
    text = ''
    text2 = ''
    prvocislo = je_prvocislo(cislo)
    if prvocislo == None:
        text='Zadané číslo nie je prirodzené číslo.'
    elif prvocislo == False:
        text=('Číslo ' + str(cislo) + ' nie je prvočíslo')
    elif prvocislo == True:
        text = ('Číslo ' + str(cislo) + ' je prvočíslo')

    if cislo < 0:
        text2 = ''
    elif cislo >= 10:
        text2='Štatistická metóda'
    elif cislo < 10:
        text2 = 'Metóda priameho delenia v cykle.'
    return [text, text2]
def test_vypocti_delitelov():
    assert vypocti_delitelov(19) == 2
    assert vypocti_delitelov(20) != 2
    # ...
def test_je_prvocislo():
    assert je_prvocislo(-1) is None
    assert je_prvocislo(3) == True
    assert je_prvocislo(4) == False
    # ...
def test_popis():
    assert popis(-1) == ['Zadané číslo nie je prirodzené číslo.','']
    assert popis(3) == ['Číslo 3 je prvočíslo','Metóda priameho delenia v cykle.']
    assert popis(12) == ['Číslo 12 nie je prvočíslo','Štatistická metóda']
    # ...
if __name__ == '__main__':
    print(popis(int(input('Zadajte ľubovoľné prirodzené číslo: '))))
