# -*- coding: utf-8 -*-
"""
.. module:: functions
   :platform: Unix, Windows
   :synopsis: just nothing
.. moduleauthor:: Matteo Caorsi

doing trivial stuff
"""

def hello_world(name):
    """
    Print `name` and greetings
    Args:
        name (str): your name
    Returns:
        None
    """
    if not isinstance(name,str):
        raise TypeError("The varaible 'name' is not a str")
    print("Hello " + name + ".")