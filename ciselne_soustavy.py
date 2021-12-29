import sys

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