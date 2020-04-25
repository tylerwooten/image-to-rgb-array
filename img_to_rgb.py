
import matplotlib.pyplot as plt
import csv
from scipy import misc
arr = misc.imread('test2_32_32.png') # 640x480x3 array

from scipy import misc
plt.imshow(arr)  # shows image that I'm importing
plt.show()

arr[1, 1]
print(arr)
print(arr[0])  # print very top row of RBG image data
with open('data.csv', 'w', newline='') as csv_file:
    for x in arr:
        for x1 in x:
                writer = csv.writer(csv_file)
                writer.writerow(x1)

