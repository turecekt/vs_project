import sys
import math

def decimalToBinary(decimal):
    print(decimal, 'je ve dvojkové soustavě:', bin(decimal)[2:])

def decimalToOctal(decimal):
    print(decimal, 'je v osmičkové soustavě:', oct(decimal)[2:])

def decimalToHexadecimal(decimal):
    print(decimal, 'je v osmičkové soustavě:', hex(decimal)[2:])

def switch(selection, n):
    if selection == 1:
        decimalToBinary(n)
    elif selection == 2:
        decimalToOctal(n)
    elif selection == 3:
        decimalToHexadecimal(n)
    
print('Zadejte kladné celé číslo v desítkové soustavě (Pro ukončení zadejte \"exit\"):')
n = input()

if n == 'exit':
        sys.exit('Program byl ukončen')

while not n.isnumeric():
    print('Zadali jste neplatnou hodnotu:', n)
    print('Musíte zadat kladné celé číslo (Pro ukončení zadejte \"exit\"):')
    n = input()
    if n == 'exit':
        sys.exit('Program byl ukončen')

while int(n) < 0:
    print('Zadali jste neplatnou hodnotu:', n)
    print('Musíte zadat kladné celé číslo (Pro ukončení zadejte \"exit\"):')
    n = input()
    if n == 'exit':
        sys.exit('Program byl ukončen')

print('Vyberte soustavu, do které chcete číšlo přenést (Pro ukončení zadejte \"exit\"):')
print('1 - Dvojková')
print('2 - Osmičková')
print('3 - Šestnáctková')

s = input()
if s == 'exit':
        sys.exit('Program byl ukončen')

while not s.isnumeric():
    print('Zadali jste neplatnou hodnotu:', s)
    print('Vyberte soustavu, do které chcete číšlo přenést (Pro ukončení zadejte \"exit\"):')
    print('1 - Dvojková')
    print('2 - Osmičková')
    print('3 - Šestnáctková')
    s = input()
    if s == 'exit':
        sys.exit('Program byl ukončen')

while not 1 <= int(s) <= 3:
    print('Zadali jste neplatnou hodnotu:', s)
    print('Vyberte soustavu, do které chcete číšlo přenést (Pro ukončení zadejte \"exit\"):')
    print('1 - Dvojková')
    print('2 - Osmičková')
    print('3 - Šestnáctková')
    s = input()
    if s == 'exit':
        sys.exit('Program byl ukončen')

switch(int(s), int(n))