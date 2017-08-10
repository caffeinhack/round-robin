#!/usr/bin/python
# coding:utf-8

'''character_list.py
Written by akakou at 2017 08/10.

This module is stationery for list of characters.
'''


class CharacterList:
    '''This class is stationery for list of characters.'''

    def __init__(self, any_characters=[], alphabets=False, numbers=False):
        '''Set up which characters using for making strings.'''
        self.character_list = any_characters
