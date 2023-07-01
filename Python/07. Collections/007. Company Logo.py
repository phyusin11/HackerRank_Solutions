#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()
    most_common_character=Counter(sorted(s)).most_common(3)

# for char,num in most_common_character:
for i in most_common_character:
    print(*i)

    

    
