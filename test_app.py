"""Test module for app class."""

import builtins
from .app import App
from .number_system import BinarySystem, OctalSystem, HexSystem


class TestApp:
    """App class tests."""

    def test_parse_input_number_ending(self):
        """Test if ending input returns proper value."""
        app = App()
        builtins.input = lambda x: '#'

        assert app.parse_input_number() is None

    def test_parse_input_valid_input(self):
        """Test if valid input returns proper value."""
        app = App()
        builtins.input = lambda x: '64'

        assert app.parse_input_number() == 64

    def test_parse_target_number_system_ending(self):
        """Test if ending input returns proper value."""
        app = App()
        builtins.input = lambda x: '#'

        assert app.parse_target_number_system() is None

    def test_parse_target_number_system_return_binary_system(self):
        """Test if proper input returns proper number system."""
        app = App()
        builtins.input = lambda x: '1'

        assert isinstance(app.parse_target_number_system(), BinarySystem)

    def test_parse_target_number_system_return_octal_system(self):
        """Test if proper input returns proper number system."""
        app = App()
        builtins.input = lambda x: '2'

        assert isinstance(app.parse_target_number_system(), OctalSystem)

    def test_parse_target_number_system_return_hex_system(self):
        """Test if proper input returns proper number system."""
        app = App()
        builtins.input = lambda x: '3'

        assert isinstance(app.parse_target_number_system(), HexSystem)
