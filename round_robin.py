#!/usr/bin/python
# coding:utf-8

'''round_robin.py
Written by akakou at 2017 08/10.

This module makes round-robin strings.
'''

import character_list
import itertools

CharacterList = character_list.CharacterList


class RoundRobin(CharacterList):
    '''This class is main class.'''

    def setup(self):
        '''Set up self data.'''
        self.string = ['']
        self.count = 0

    def next(self):
        '''Set next string and return it.'''
        self.setup()

        while True:
            self.count += 1
            for self.string in itertools.product(
                self.character_list,
                repeat=self.count
            ):
                yield self.get_string()

    def get_string(self):
        '''Return self.string.'''
        return ''.join(self.string)
