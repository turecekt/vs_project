"""Test for number system classes."""

from .number_system import BinarySystem, OctalSystem, HexSystem


class TestNumberSystem:
    """Number system testing class."""

    def test_convert_decimal_to_binary(self):
        """Test binary system conversion method."""
        binary_number_system = BinarySystem()

        assert binary_number_system.convert_decimal(64) == '0b1000000'

    def test_convert_decimal_to_octal(self):
        """Test octal system conversion method."""
        octal_number_system = OctalSystem()

        assert octal_number_system.convert_decimal(64) == '0o100'

    def test_convert_decimal_to_hex(self):
        """Test hex system conversion method."""
        hex_number_system = HexSystem()

        assert hex_number_system.convert_decimal(64) == '0x40'
