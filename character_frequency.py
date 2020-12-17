#!/usr/bin/env python3

##########################################################################
# Project: AK1VS - Final project
# Description: This project should show how to work with versioning tool such
#              as git.
# Task: Character rate
#       - Input:    text file as parameter
#                   StdIn in case of no parameter (reading upon '#')
#       - Output:   character count
#                   most frequent character
#                   least frequent character
#                   average occurence of character
#                   frequency of each alphabetic character
#############################################################################
# UTB Zlin - FAI 2020
# Author: Adam Huspenina

import sys
import argparse
import statistics


##########################################################################
# Class contains whole functionality needed for completing deisred tasks.
class CharacterFrequency:
    def __init__(self, intput):
        self.input = intput
        self.char_dict = self._init_dictionary()

    ##########################################################################
    # Method returns touple of most frequent character list
    # (list because of equalities).
    def get_most_frequent(self):
        max_value = max(self.char_dict.values())
        max_keys = []
        for k, v in self.char_dict.items():
            if v == max_value:
                max_keys.append(k)
        return (max_keys, max_value)

    ##########################################################################
    # Method returns touple of least frequent character list
    # (list because of equalities).
    def get_least_frequent(self):
        min_value = min(self.char_dict.values())
        min_keys = []
        for k, v in self.char_dict.items():
            if v == min_value:
                min_keys.append(k)
        return (min_keys, min_value)

    ##########################################################################
    # Method returns touple of average occurence of character list
    # (list because of equalities).
    def get_average(self):
        avg_value = statistics.mean(self.char_dict.values())
        rounded_value = round(avg_value)
        avg_keys = []
        for k, v in self.char_dict.items():
            if v == rounded_value:
                avg_keys.append(k)
        return (avg_value, avg_keys)

    ##########################################################################
    # Method returns list of alphabetic character with their frequency
    # of occurence.
    def get_alpha_frequency(self):
        alpha_dict = {}
        for k, v in self.char_dict.items():
            if k.isalpha():
                alpha_dict[k] = v
        return alpha_dict

    ##########################################################################
    # Method for printing lists with result.
    def output(self, output_list):
        print(str(output_list))

    ##########################################################################
    # Private method read input data and store them into dictionary.
    # For stdin dictionary contains only characters until '#' is read.
    # 'DEBUG' option is for testing purposes, when tester can easily handle
    # input. It can be only reached through code.
    # Tester has to define self.char_dict by him self.
    def _init_dictionary(self):
        character_dict = {}
        if (self.input != 'DEBUG'):
            if (self.input == '<stdin>'):
                while True:
                    char = sys.stdin.read(1)
                    if (char == '#'):
                        break
                    dict_keys = character_dict.keys()
                    if (char in dict_keys):
                        character_dict[char] += 1
                    else:
                        character_dict[char] = 1
            else:
                file_input = open(self.input, 'r')
                while True:
                    char = file_input.read(1)
                    if (char == ''):
                        break
                    dict_keys = character_dict.keys()
                    if (char in dict_keys):
                        character_dict[char] += 1
                    else:
                        character_dict[char] = 1
            file_input.close()
        return character_dict


##########################################################################
# Outter method for parsing input arguments from terminal.
def parse_args():
    parser = argparse.ArgumentParser(
        description="Get information about character frequency form input.")
    parser.add_argument("-i", nargs='?',
                        help="File containing characters to be analyzed.",
                        type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    return args


##########################################################################
# Driving method for whole program.
def main(args):
    characters = CharacterFrequency(args.i.name)
    # Print most frequent value with corresponding characters.
    characters.output(characters.get_most_frequent())
    # Print least frequent value with corresponding characters.
    characters.output(characters.get_least_frequent())
    # Print average rate value with characters having rounded average rate.
    characters.output(characters.get_average())
    # Print alphabetic characters rate.
    characters.output(characters.get_alpha_frequency())


if __name__ == "__main__":
    args = parse_args()
    main(args)
