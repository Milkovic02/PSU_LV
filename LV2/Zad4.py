import numpy as np
import matplotlib.pyplot as plt

firstQ = np.zeros((50, 50))
print(firstQ)
secondQ = np.full((50, 50), 255)
print(secondQ)

firstH = np.hstack((firstQ, secondQ))
secondH = np.hstack((secondQ, firstQ))

img = np.vstack((firstH, secondH))

plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
