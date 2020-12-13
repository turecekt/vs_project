import math
print("Zadejte souřadnice pro bod A na ose X: ")
ax = input()
print("Zadejte souřadnice pro bod A na ose Y: ")
ay = input()
print("Zadejte souřadnice pro bod B na ose X: ")
bx = input()
print("Zadejte souřadnice pro bod B na ose Y: ")
by = input()
print("Zadejte souřadnice pro bod C na ose X: ")
cx = input()
print("Zadejte souřadnice pro bod C na ose Y: ")
cy = input()
stra1 = bx-cx
stra2 = by-cy
stra1 = math.pow(2, stra1)
stra2 = math.pow(2, stra2)
stra = math.sqrt(stra1+stra2)
print("Délka strany a: " + stra + "cm")
strb1 = cx-ax
strb2 = cy-ay
strb1 = math.pow(2, strb1)
strb2 = math.pow(2, strb2)
strb = math.sqrt(strb1+strb2)
print("Délka strany b: " + strb + "cm")
strc1 = ax-bx
strc2 = ay-by
strc1 = math.pow(2, strc1)
strc2 = math.pow(2, strc2)
strc = math.sqrt(strc1+strc2)
print("Délka strany c: " + strc + "cm")
if stra + strb > strc and strb + strc > stra and strc + stra > strb:
    print("Trojúhelník je sestrojitelný")
else:
    print("Trojúhelník není sestrojitelný")
obvod = stra + strb + strc
print("Obvod trojúhelníku je " + obvod + "cm")
s = (stra + strb + strc) / 2
obsah = math.sqrt(s * (s - stra) * (s - strb) * (s - strc))
print("Obsah trojúhelníku je" + obsah + "cm")
if math.pow(2, stra) == math.pow(2, strb) + math.pow(2, strc) or math.pow(2, strb) == math.pow(2, strc) + math.pow(2, stra) or math.pow(2, strc) == math.pow(2, stra) + math.pow(2, strb):
    print("Trojúhelník je pravoúhlý")
else:
    print("Trojúhelník není pravoúhlý")