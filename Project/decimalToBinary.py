def convert(dec_num):
    if dec_num == 0:
        return 0
    else:
        convert(int(dec_num / 2))
        return dec_num % 2
