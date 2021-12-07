
def sestrojitelnost():
  if ( (a+b)>c ) and ( (a+c)>b ) and ( (b+c)>a ):
     print("Trojuhelnik je sestrojitelny")
  else: 
      print("Trojuhelnik neni sestrojitelny")

def informace():
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    max=a
    min=a
    #Nejdelsi strana
    if b>max:       
        max=b
    if c>max:
        max=c
   #Nejkratsi strana
    if b<min:
        min=b
    if c<min:
        min=c
    #Vypis max
    if (max==a):
        print("Nejdelsi strana: a = "+str(max))
    if (max==b):
        print("Nejdelsi strana: b = "+str(max))
    if (max==c):
        print("Nejdelsi strana: c = "+str(max))
    #Vypis min 
    if (min==a):
        print("Nejkratsi strana: a = "+str(min))
    if (min==b):
        print("Nejkratsi strana: b = "+str(min))
    if (min==c):
        print("Nejkratsi strana: c = "+str(min))

def obvod_obsah():
    O=a+b+c
    s=O/2
    S=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Obvod: "+str(O)+"\n"+"Obsah: "+str(S))

def pravouhlost():
    if (c==math.sqrt( a**2 + b**2 )):
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")

sestrojitelnost()
informace()
obvod_obsah()
pravouhlost()