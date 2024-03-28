import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("C:\Users\student\PSU\LV2\tiger.png")
druga_cetvrtina = img[0 : img.shape[0], img.shape[1] // 4 : img.shape[1] // 2].copy()
rotated = np.rot90(img.copy(), k=1, axes=(1, 0))
img_cpy = img[:, :, 0].copy()
value = 200
lim = 255 - value

for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        if img_cpy[x][y] > lim:
            img_cpy[x][y] = 255
        else:
            img_cpy[x][y] += value

mirror_img = np.fliplr(img)

plt.figure()
plt.imshow(img_cpy, cmap="gray")
plt.show()

plt.figure()
plt.imshow(druga_cetvrtina, cmap="gray")
plt.show()

plt.figure()
plt.imshow(rotated, cmap="gray")
plt.show()

plt.figure()
plt.imshow(mirror_img, cmap="gray")
plt.show()

smanjena = img.reshape(img.shape[0] // 10, 10, img.shape[1] // 10, 10).mean(axis=(1,3)) 
plt.figure()
plt.imshow(smanjena, cmap="gray")
plt.title("smanjena slika")

