'''
DRAČÍKŘIVKA
Vytvořte program, který vykreslí Dračí křivku, někdy nazývanou „Heighway Dragon“.
VSTUP•
Počet iterací Dračí křivky •
Barva vykreslené čáry (z výčtu)•
Barva pozadí (z výčtu)•
Vpřípadě puštění bez parametrů vykreslení 9-té iterace Dračí křivky, červenoučárou na černém pozadí
VÝSTUP•
Vykreslení a zobrazení Dračí křivky
'''

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


'''
	Input values
'''
iteration=int(input('Pocet interakci:'))
linecolor=input('Barva cary:')
backgroundcolor=input('Barva pozadi:')



