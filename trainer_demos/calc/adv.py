#! /usr/bin/env python3
# Author: DCameron
# Description: This module contains a collection of advanced calculator functions
"""
    Advanced Calc functions including mod, power, and sqrt
"""

import sys

def mod(x, z):
    """ Return REMAINDER of x divided by z """
    return x % z

def power(x, z):
    """ Return POWER of x to z """
    return x**z

def sqrt(x):
    """ Return square root of x """
    return round(x**0.5, 2)

print("ADVANCED Calculator App")
print("-" * 30)

print(f"100 % 30 = {mod(100, 30)}")
print(f"100 ** 3 = {power(100, 3)}")
print(f"\N{square root}100 = {sqrt(100)}")

sys.exit(0)