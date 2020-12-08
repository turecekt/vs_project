userInp = input('Zadejte cele cislo na preklad :')
userInp = int(userInp)

class romanNum:

    def intToRom(self, userInp):

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
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