class romanNum:

    def intToRom(self, num):
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
        while  num > 0:
            for _ in range(num // val[i]):
                transNum += syb[i]
                num -= val[i]
            i += 1
        return transNum


print(romanNum().intToRom(1))
print(romanNum().intToRom(4021)) 