#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#

def carParkingRoof(cars, k):
    cars = sorted(cars)
    ## Version 1
    window = cars[0 + k - 1] - cars[0] + 1
    result = window
    
    for i in range(1, len(cars) - k):
        j = i + k - 1
        window = cars[j] - cars[i] + 1
        result = min(result, window)
        
    return result

    ## Version 2
    # minDist = abs(cars[0] - cars[-1]) + 1
    # for i in range(len(cars) - k):
    #     roofDist = abs(cars[i] - cars[i + k - 1]) + 1
    #     minDist = min(minDist, roofDist)
    
    # return minDist

if __name__ == '__main__':
