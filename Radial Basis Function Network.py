import math
import random

import numpy as np

def calculate(input1, input2, diemension, weight, quantity, k):
    numerator = 0
    q = 1
    input = np.zeros([diemension])
    for x in range(quantity):
        for y in range(diemension):
            input[x] = input[x] + math.exp(-1*(math.pow(math.fabs(input2[y] - input1[x, y]), 2)/ (2 *(math.pow(q, 2)))))
        for a in range(k):
            numerator += input[x] * weight[a]
    return numerator

if __name__ == '__main__':
    diemension = 3
    quantity = 3
    k = 5 # number of neurons
    i = np.zeros([quantity, diemension])
    j = np.zeros([diemension])
    weight = np.zeros([k])
    for x in range(quantity):
        for y in range(diemension):
            i[x, y] = random.randint(0, 10) * random.random()

    for x in range(diemension):
        v = input()
        temp = float(v)
        j[x] = temp
    for x in range(k):
        weight[x] = random.randint(0, 10) * random.random()
    score = calculate(i, j, diemension, weight, quantity, k)
    print(score)