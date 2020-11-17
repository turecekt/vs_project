def convert(num):
    binar=''
    if num == 0:
        binar='0'+binar
    else:
        while num>0:
            binar=str(num%2)+binar
            num=num//2
    return binar
