import argparse

A = ".-"
B = "-..."
C = "-.-."
D = "-.."
E = "."
F = "..-."
G = "--."
H = "...."
CH = "----"
I = ".."
J = ".---"
K = "-.-"
L = ".-.."
M = "--"
N = "-."
O = "---"
P = ".--."
Q = "--.-"
R = ".-."
S = "..."
T = "-"
V = "...-"
W = ".--"
X = "-..-"
Y = "-.--"
Z = "--.."

msg = "type in the string consist of morse code or alphabet"

parser = argparse.ArgumentParser(description = msg)

str = parser.parse_args()

print("string % s" %str)

""" /be careful about anything else than alphabet and dots and commas

"""

""" upper() """
    