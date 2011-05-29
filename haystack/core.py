# -*- coding: utf-8 -*-

"""
haystack.core
~~~~~~~~~~~~~

This module contains the core Haystack functionality.
"""


from random import random



def maths(*args, **kwargs):
    """Does all the maths."""

    return random()


def main():
    print 'Random Number: {0}'.format(maths())



if __name__ == '__main__':
    main()
