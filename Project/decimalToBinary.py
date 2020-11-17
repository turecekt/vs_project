# Function that converts decimal number to binary number
def convert(num):
    binar = ''
    if num == 0:
        binar = '0' + binar
    else:
        # Cycle and divide number that is higher than 0
        while num > 0:
            binar = str(num % 2) + binar
            num = num // 2
    # Returns converted binary number
    return binar
