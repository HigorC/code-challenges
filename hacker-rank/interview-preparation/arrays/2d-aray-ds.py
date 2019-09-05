# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    max = -(math.inf)

    for i in range(1,5):
        for j in range(1, 5):
            sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            sum += arr[i][j]
            sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

            if sum > max: max = sum

    return max

if __name__ == '__main__':

    fptr = open("C:\\***CAMINHO-PARA-ESCREVER-RESPOSTA***\\res.txt", 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()