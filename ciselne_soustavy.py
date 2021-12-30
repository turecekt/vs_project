import sys

# vycet cislic pro soustavy se zakladem 2 az po cislice se zakladem 32
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	'''
	Program prevede zadane cislo <cislo> z desitkove soustavy
	do ciselne soustavy se zakladem <cilova_ciselna_soustava>.
	'''

	cislo, cilova_ciselna_soustava = nactiVstup()

	print(f'Zadane cislo: {cislo}, zaklad vybrane soustavy: {cilova_ciselna_soustava}, prevedene cislo: {preved(cislo, cilova_ciselna_soustava)}')	# noqa: E501
	input('Stisknete ENTER pro ukonceni.')


def nactiVstup():
	'''
	Metoda nactiVstup nacte parametry <cislo> a <cilova_ciselna_soustava> budto z predanych parametru pri spusteni programu,
	nebo je necha zadat uzivatelem programu, nebo vypise napovedu.
	'''

	# kontrola jestli jsou pri spousteni programu predavane parametry
	if len(sys.argv) > 1:
		args = sys.argv[1:]

		# kontrola jestli bylo pozadovano vypsani napovedy
		if args[0] == 'help' or args[0] == '-h':
			print('Spustte budto s parametry: <cislo> <cilova_ciselna_soustava>(2..32), nebo help (-h) pro vypsani napovedy, nebo bez parametru pro rucni zadani hodnot uzivatelem.')  # noqa: E501
			exit(0)
		else:
			# nacteni parametru <cislo> a <cilova_ciselna_soustava> pri spusteni programu
			try:
				cislo = int(args[0])
				cilova_ciselna_soustava = int(args[1])
				if cilova_ciselna_soustava < 2 or cilova_ciselna_soustava > 32:
					print('Parametr <cilova_ciselna_soustava>(2..32) je mimo povoleny rozsah 3..32.')
				return cislo, cilova_ciselna_soustava
			except BaseException:
				print('Nespravne zadane parametry: <cislo> <cilova_ciselna_soustava>(2..32)')

	# nacitani parametru <cislo> od uzivatele
	cislo = zadejCislo()

	# nacitani parametru <cilova_ciselna_soustava> od uzivatele
	cilova_ciselna_soustava = zadejSoustava()

	return cislo, cilova_ciselna_soustava


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


if __name__ == '__main__':
	main()


# Pytest testy
def testPreved():
	assert preved(98, 17) == '5D'


def testZadejCislo(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: 5)
	assert zadejCislo() == 5


def testZadejSoustava(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: 10)
	assert zadejSoustava() == 10
