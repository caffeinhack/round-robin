#!/usr/bin/python
# coding:utf-8

'''character_list.py
Written by akakou at 2017 08/10.

This module is stationery for list of characters.
'''

import string


class CharacterList:
    '''This class is stationery for list of characters.'''

    def __init__(
            self,
            any_characters=[],
            use_alphabets=False,
            use_large_alphabets=False,
            use_small_alphabets=False,
            use_numbers=False,
            use_all=False
            ):
        '''Set up which characters using for making strings.'''
        self.reset()
        self.add_any(any_characters)

        # Check using all and
        # add to character list.
        if use_all:
            self.add_alphabets()
            self.add_numbers()
            return

        # Check using alphabets and
        # add to character_list.
        if use_alphabets:
            self.add_alphabets()
        else:
            # Check using small and large alphabets so.
            if use_small_alphabets:
                self.add_small_alphabets()
            elif use_large_alphabets:
                self.add_large_alphabets()

        # Check using numbers and
        # add to character_list.
        if use_numbers:
            self.add_numbers()

    def reset(self):
        '''Reset character_list.'''
        self.character_list = []

    def add_any(self, any_characters):
        '''Add any list of character.'''
        # check variable type
        if not isinstance(any_characters, list):
            any_characters = list(any_characters)
        self.character_list.extend(any_characters)

    def add_alphabets(self):
        '''Add alphabets.'''
        all_alphabets = string.ascii_letters
        self.add_any(all_alphabets)

    def add_small_alphabets(self):
        '''Add small alphabets.'''
        all_alphabets = string.ascii_letters
        self.add_any(all_alphabets[0:26])

    def add_large_alphabets(self):
        '''Add large alphabets.'''
        all_alphabets = string.ascii_letters
        self.add_any(all_alphabets[26:])

    def add_numbers(self):
        '''Add numbers.'''
        # make character list of numbers
        numbers = []
        for count in range(0, 10):
            count = str(count)
            numbers.append(count)

        self.add_any(numbers)
