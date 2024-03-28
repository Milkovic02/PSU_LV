import numpy as np
import matplotlib.pyplot as plt


plt.plot([2, 3], [2, 2], "r", linewidth=1, marker=".", markersize=5)
plt.plot([3, 3], [2, 1], "g", linewidth=1, marker=".", markersize=5)
plt.plot([3, 1], [1, 1], "b", linewidth=1, marker=".", markersize=5)
plt.plot([1, 2], [1, 2], "b", linewidth=3, marker=".", markersize=5)
plt.axis([0, 4, 0, 4])
plt.title("Primjer")
plt.xlabel("x-os")
plt.ylabel("y-os")
plt.show()
