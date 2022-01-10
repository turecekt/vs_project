"""Module with number system representations."""

from abc import ABC, abstractmethod


class NumberSystem(ABC):
    """Abstract class to number systems."""

    @abstractmethod
    def convert_decimal(self, number):
        """Abstract method to convert decimal number."""
        pass


class BinarySystem(NumberSystem):
    """Class representing binary number system."""

    def convert_decimal(self, number):
        """Convert decimal number into binary one."""
        return bin(number)


class OctalSystem(NumberSystem):
    """Class representing octal number system."""

    def convert_decimal(self, number):
        """Convert decimal number into octal one."""
        return oct(number)


class HexSystem(NumberSystem):
    """Class representing hexadecimal number system."""

    def convert_decimal(self, number):
        """Convert decimal number into hex one."""
        return hex(number)
