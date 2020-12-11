import math

def is_valid(a, b, c):
    return a + b > c and a + c > b and b + c > a

def area(a, b, c):
    # Heron's formula
    s = (a + b + c) / 2 # the semiperimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def is_right_angle(a, b, c):
    pow_a = a ** 2
    pow_b = b ** 2
    pow_c = c ** 2
    return (math.isclose(pow_a, pow_b + pow_c)
         or math.isclose(pow_b, pow_a + pow_c)
         or math.isclose(pow_c, pow_a + pow_b))
