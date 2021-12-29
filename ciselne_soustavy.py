import sys

# vycet cislic pro soustavy se zakladem 2 az po cislice se zakladem 32
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

def zadejCislo():
	'''
	Metoda zadejCislo() nacte parametr <cislo>, ktere zada uzivatel, pri spatnem zadani vypise chybu a necha uzivatele opakovat
	'''

	while True:
		try:
			cislo = int(input('Zadejte kladne cele cislo: '))
			if cislo > 0:
				return cislo
			else:
				print('Spatny vstup. Zadejte pouze kladne cele cislo.')
		except BaseException:
			print('Spatny vstup. Zadejte pouze kladne cele cislo.')


def zadejSoustava():
	'''
	Metoda zadejSoustava() nacte parametr <cilova_ciselna_soustava>, kterou zada uzivatel,
	pri spatnem zadani vypise chybu a necha uzivatele opakovat
	'''
	while True:
		try:
			cilova_ciselna_soustava = int(input('Zadejte cilovou ciselnou soustavu (2..32): '))
			if cilova_ciselna_soustava <= 32 and cilova_ciselna_soustava >= 2:
				return cilova_ciselna_soustava
		except BaseException:
			print('Spatny vstup. Zadejte cilovou ciselnou soustavu jako cele kladne cislo.')
		else:
			print('Spatny vstup. Zadejte cilovou ciselnou soustavu v rozsahu intervalu (2..32)')
			
def preved(cislo: int, cilova_ciselna_soustava: int) -> str:
	'''
	Metoda preved prevede <cislo> z desitkove soustavy do ciselne soustavy se zakladem <cilova_ciselna_soustava>
	'''

	# cislo se bude nejprve ukladat do pole znaku
	prevedene = []

	prevedene.append(DIGITS[cislo % cilova_ciselna_soustava])
	cislo //= cilova_ciselna_soustava

	while cislo:
		prevedene.append(DIGITS[cislo % cilova_ciselna_soustava])
		cislo //= cilova_ciselna_soustava

	# pole znaku se prevede na string ve spravnem (opacnem nez bylo vkladane do pole) poradi
	vysledek = ''
	for s in prevedene[::-1]:
		vysledek += s
	return vysledek
