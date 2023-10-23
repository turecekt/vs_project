
Program Morseovka
-----------------

morse.py po vyvolani precte argumenty na prikazovem radku,
nebo zacne cist stdin, pokud zadny argument nebyl zadan, vysledny
text je povazovan za vstup. pokud vstup obsahuje jen znaky
morseovy abecedy ('.-/, \n') je decodovan, jinak je cely vstup codovan
v morseove abecede. platny syntax morseovy abecedy je:
 * '.' - tecka,
 * '-' - carka,
 * '/' - mezera mezi pismeny
 * ',' - mezera mezi slovy
 * ' ', '\n' - ignorovane znaky

priklad platneho textu v morseove abecede:
"...././.-../.-../---/,/.--/---/.-./.-../-.." ("hello world")
