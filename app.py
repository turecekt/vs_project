from number_system import *

"""
Base App class to run this application.
"""


class App:

    """
        Base function to run this app.
    """

    def run(self):
        App.print_help()

        input_number = self.parse_input_number()

        if input_number is None:
            print("Program end requested. Exiting...")
            return

        target_number_system = self.parse_target_number_system()

        print(target_number_system.convert_decimal(input_number))

    """
        Method to handle user input. Return valid integer or None if program end is wanted.
    """

    def parse_input_number(self):
        number = input("Please pass unsigned integer: ")

        try:
            if self.is_ending(number):
                return None

            number = int(number)

            if number < 0:
                raise ValueError

        except ValueError:
            print("Not a valid unsigned integer! Please try once again.")
            return self.parse_input_number()

        return number

    """
        Method to handle user target system input.
    """
    def parse_target_number_system(self):
        target_system = input("Please choose target number system: ")

        try:
            if self.is_ending(target_system):
                return None

            target_system = int(target_system)

            if target_system not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Not a valid target system! Please try once again.")
            return self.parse_target_number_system()

        if target_system == 1:
            return BinarySystem()

        if target_system == 2:
            return OctalSystem()

        return HexSystem()

    """
        Method to check ending string
    """
    @staticmethod
    def is_ending(char):
        if char == "#":
            return True

        return False

    """
        Function which prints help text to understand, how to use this app.
    """

    @staticmethod
    def print_help():
        print("You can convert numbers from decimal system to binary, octal or hex systems.")
        print("At first you need to pass number in decimal system.")
        print("Then you need to choose target number system by selecting number.")
        print("1. Binary")
        print("2. Octal")
        print("3. Hex")
        print("At final enjoy your result.")
