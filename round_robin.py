#!/usr/bin/python
# coding:utf-8

'''round_robin.py
Written by akakou at 2017 08/10.

This module makes round-robin strings.
'''


class RoundRobin:
    '''This class is main class.'''

    def __init__(self, any_characters=[], alphabets=False, numbers=False):
        '''Set up which characters using for making strings.'''
        self.characters = any_characters
