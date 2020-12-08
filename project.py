userInp = input('Zadejte cele cislo na preklad :')  #Tohle vezme input od uzivatele
userInp = int(userInp) #Tohle prevede input od uzivatele na int aby to program mohl zpracovat

class romanNum:

#Vytvorime funcki ktera vezme userInp jako vstupni parametr
    def intToRom(self, userInp):

#Nadefinujeme si cisla na ktere pak budem odkazovat
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
#Nadefinujeme si symboly na ktere pak budem odkazovat
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        transNum = ''
        i = 0
        while  userInp > 0:
            for _ in range(userInp // val[i]):
                transNum += syb[i]
                userInp -= val[i]
            i += 1
        return transNum


print(romanNum().intToRom(userInp))