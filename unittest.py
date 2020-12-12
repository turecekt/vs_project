#UNIT TEST 1
def unitTest1():
    result = "... --- ... "
    s = "sos"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 2
def unitTest2():
    result = "...-- -.... ..... "
    s = "365"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 3
def unitTest3():
    result = "...- . .-.. .. -.- --- ... - "
    s = "vEliKoSt"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 4
def unitTest4():
    result = "-.-. .. ... .-.. --- ....- ..--- "
    s = "Cislo42"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 5
def unitTest5():
    result = ".- .... --- .---   .--- .- -.-   ... .   -- .- ..."
    s = "Ahoj jak se mas"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")
