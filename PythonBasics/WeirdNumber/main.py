#!/bin/python3

import math
import os
import random
import re
import sys

def WeirdNumber(n):
    if n % 2 != 0:
        print('Weird')
    elif n in range(2, 5) and n % 2 == 0:
        print('Not Weird')
    elif n in range(6, 21) and n % 2 == 0:
        print('Weird')
    elif n > 20 and n % 2 == 0:
        print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())
    WeirdNumber(n)
