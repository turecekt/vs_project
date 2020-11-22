"""
function to calculate hexadecimal number from decimal number.

input -> decimal number
output -> hexadecimal number
"""


def convert(input_number):
    """Convert decimal number to hexadecimal."""
    input_number = int(input_number)
    x = (input_number % 16)  # modulo
    chars = "0123456789ABCDEF"
    rest = input_number / 16  # rest after division

    # if rest equals zero, return characters where index is x
    if rest == 0:
        return chars[x]
    # if rest is not zero, use method "convert" recursively
    return convert(rest) + chars[x]
