# Četnost znaků
Tento repozitář slouží jako závěrečný projekt z předmětu AP1VS.

## Vstup
* Textový soubor (obsahující text bez diakritiky) jako parametr programu
* V případě spuštění bez parametru musí program umět zpracovat text ze  
standardního vstupu až po řádek obsahující ukončovací symbol #

## Výstup
* Informace o celkovém počtu znaků
* Informace o nejčastějším znaku
* Informace o nejméně častém znaku
* Informace o průměrné četnosti
* Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)

## Ukázka spuštění programu
### Spuštění programu bez parametru:
`py main.py`  

Program nechá uživatele zadávat textové řetězce, dokud řádek neobsahuje ukončovací symobl #.

`Zadejte textový řetězec: naolejujelijuliekoleje`

`Zadejte textový řetězec: nebonenaolejujejuliekoleje#`

#### Výstup:
```
Celkový počet znaků: 48
Nejméně častý znak: 'b'
Nejčastější znak: 'e'
Průměrná četnost: 4.8
Četnost jednotlivých znaků abecedy:
ZNAK|ČETNOST     |NR.
   a|**          |2
   b|*           |1
   e|************|12
   i|***         |3
   j|********    |8
   k|**          |2
   l|*******     |7
   n|****        |4
   o|*****       |5
   u|****        |4
```

### Ukázka spuštění se souborem "random_text.txt" jako parametrem
`py main.py random_text.txt`

#### Částečný výstup:
```
Celkový počet znaků: 256
Nejméně časté znaky: ['X', 'd', 'T', '2', '6', 'P', 'K', 'U']
Nejčastější znak: '3'
Průměrná četnost: 4.13
Četnost jednotlivých znaků abecedy:
ZNAK|ČETNOST |NR.
   A|***     |3
   B|******  |6
   C|*****   |5
   D|*****   |5
   E|********|8
   F|**      |2
   G|**      |2
   H|***     |3
   I|**      |2
   J|****    |4
   K|*       |1
        .
        .
        .
```