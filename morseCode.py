import argparse
import re
import sys

letter_a = ".-"
letter_b = "-..."
letter_c = "-.-."
letter_d = "-.."
letter_e = "."
letter_f = "..-."
letter_g = "--."
letter_h = "...."
letter_ch = "----"
letter_i = ".."
letter_j = ".---"
letter_k = "-.-"
letter_l = ".-.."
letter_m = "--"
letter_n = "-."
letter_o = "---"
letter_p = ".--."
letter_q = "--.-"
letter_r = ".-."
letter_s = "..."
letter_t = "-"
letter_v = "...-"
letter_w = ".--"
letter_x = "-..-"
letter_y = "-.--"
letter_z = "--.."

msg = "type in the string consist of morse code or alphabet"

parser = argparse.ArgumentParser(description = msg)

parser.add_argument('MorseString', metavar='String', type=str, help='a string to decode/Ncode from/to morse code')

st = parser.parse_args()

matchObj = re.match(r'(.*)[^a-zA-Z \-.|]', st.MorseString, re.I)

if matchObj:
    print ("sys exit")
    sys.exit("please type in right characters")
else:
    print ("%s" %st.MorseString)
    

"""print("%s" %st)"""
print("string %s" %letter_a)



""" /be careful about anything else than alphabet and dots and commas
    extremely careful for \ ""
"""

""" upper() """
    