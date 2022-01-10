from abc import ABC, abstractmethod

"""
    Abstract class to custom number systems. 
"""


class NumberSystem(ABC):

    """
        Abstract method to convert decimal number into number system given class provides.
    """
    @abstractmethod
    def convert_decimal(self, number):
        pass


"""
    Class representing binary number system.
"""


class BinarySystem(NumberSystem):

    """
        Method to convert decimal number into binary one.
    """
    def convert_decimal(self, number):
        return bin(number)


"""
    Class representing octal number system.
"""


class OctalSystem(NumberSystem):

    """
        Method to convert decimal number into octal one.
    """
    def convert_decimal(self, number):
        return oct(number)


"""
    Class representing hexadecimal number system.
"""


class HexSystem(NumberSystem):

    """
        Method to convert decimal number into hex one.
    """
    def convert_decimal(self, number):
        return hex(number)
