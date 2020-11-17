"""
Package for DV project.

Method char_frequency takes an input text
and prints out stats regarding character frequency
"""
from .character_frequency import get_input, count_char_freq, calculate_stats

__all__ = ['get_input', 'count_char_freq', 'calculate_stats']
