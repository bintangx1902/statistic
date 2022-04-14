from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array([
    134, 25, 63, 74, 82, 98, 53, 77, 84, 134,
    47, 79, 111, 102, 42, 46, 80, 59, 67, 83,
    85, 96, 54, 87, 92, 81, 104, 64, 89, 55,
    81, 64, 72, 49, 116, 90, 78, 51, 99, 121,
    76, 33, 84, 75, 46, 135, 93, 68, 107, 63
])

below = min(data)
top = max(data)
total = len(data)

n_class = 1 + 3.3 * np.log10(total)
r_class = round(n_class)
class_width = (top - below) / r_class
r_width = round(class_width)

low_class = []
top_class = []

count = 1

while True:

    if count == 1:
        low = below
        high = low + r_width - 1
        count += 1

    else:
        low = top_class[-1] + 1
        high = low + r_width - 1
        count += 1

    low_class.append(low)
    top_class.append(high)

    print(f"{low}, {high}")

    if not top_class[-1] < (top + 1):
        break


fi = []
for ind, val in enumerate(low_class):
    count = 0
    for d in data:
        if val <= d <= top_class[ind]:
            count += 1
    fi.append(count)

print(fi)
fk1 = []
num = 0
for ind, val in enumerate(fi):
    if ind == 0:
        fk1.append(val)
    elif ind == 1:
        num += (val + fi[ind-1])
        fk1.append(num)
    else:
        num += val
        fk1.append(num)

print(fk1)

fk2 = []
limit = len(fi) + 1
for ind, val in enumerate(fi):
    fk2.append(sum(fi[ind: limit]))

print(fk2)
