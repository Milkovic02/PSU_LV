import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("C:\Users\student\PSU\LV2\mtcars.csv", "rb"), usecols=(1, 2, 3, 4, 5, 6),
                  delimiter=",", skiprows=1)

print("min mpg: ", min(data[:, 0]))
print("max mpg: ", max(data[:, 0]))
print("avg mpg: ", sum(data[:, 0])/len(data[:, 0]))

arr = data[:, 1] == 6


plt.scatter(data[:, 0], data[:, 3], c='lime',
            ec='k', s=data[:, 5]*16, marker="h")

for i, label in enumerate(data[:, 5]):
    plt.text(data[i, 0], data[i, 3]+5, str(data[i, 5]))

print("min mpg sa 6 cyl: ", min(data[arr, 0]))
print("max mpg sa 6 cyl: ", max(data[arr, 0]))
print("avg mpg sa 6 cyl: ", sum(data[arr, 0])/len(data[arr, 0]))

plt.show()