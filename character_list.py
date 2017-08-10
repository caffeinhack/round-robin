#!/usr/bin/python
# coding:utf-8

'''character_list.py
Written by akakou at 2017 08/10.

This module is stationery for list of characters.
'''

import string


class CharacterList:
    '''This class is stationery for list of characters.'''

    def __init__(self, any_characters=[], alphabets=False, numbers=False):
        '''Set up which characters using for making strings.'''
        self.character_list = any_characters

    def add_any(self, any_characters=[]):
        '''Add any list of character.'''
        self.character_list.append(any_characters)

    def add_alphabets(self):
        '''Add alphabets.'''
        all_alphabets = string.ascii_letters
        self.add_any(all_alphabets)

    def add_small_alphabets(self):
        '''Add small aplphabets.'''
        all_alphabets = string.ascii_letters
        self.add_any(all_alphabets[0:26])

    def add_large_alphabets(self):
        '''Add large aplphabets.'''
        all_alphabets = string.ascii_letters
        self.add_any(all_alphabets[26:])

    def add_integers(self):
        '''Add integers.'''
        # make character list of integers
        integers = []
        for count in range(0, 9):
            count = str(count)
            integers.append(integers)

        self.add_any(integers)
