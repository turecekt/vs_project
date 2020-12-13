# Prokejt do VS
Projekt do předmětu Nástroje pro vývoj softwarových projektů.

## Autor
Ondřej Marýzek <br/>
<o_maryzek@utb.cz> <br/>
Os. číslo: **A20522**

## Zadání - Trojúhelník

### Vstup
- Souřadnice vrcholů (tří bodů) ve 2D prostoru
- Program musí mít implementovánu alespoň jednu z následujících možností zadávání souřadnic:
    - Předávání souřadnic pomocí parametrů při spuštění, nebo
    - Zadávání souřadnic za běhu programu dotazováním uživatele

### Výstup
- Informace o sestrojitelnosti trojúhelníku
- Informace o délkách stran
- Informace o obvodu a obsahu
- Informace o pravoúhlosti

## Návod na použití
body trojúhelníku lze zadat buď pomocí argumentů příkazové řádky

```
python main.py <Ax> <Ay> <Bx> <By> <Cx> <Cy>
```
např.: `python main.py 0 0 100 0 0 100`

nebo interaktivně (bez argumentů příkazové řádky)
```
python main.py
```

kdy se program ptá na souřadnice jednotlivých bodů. Souřadnice jednoho bodu se zadávají jako dvě čísla oddělená mezerou, např.:
```
Zadejte souřadnice bodu A
-50 50.5
```
