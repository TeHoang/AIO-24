import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('./dog.jpeg')

gray_img_01 = (np.max(img, axis=-1, keepdims=1) +
               np.min(img, axis=-1, keepdims=1)) / 2

# Lightness
print(gray_img_01[0, 0])  # [102.5]

# Average
gray_img_02 = np.average(img, axis=-1, keepdims=1)
print(gray_img_02[0, 0])  # [107.7]

# Luminosity
luminosity_constant = [0.21, 0.72, 0.07]
gray_img_03 = np.dot(img[..., :3], luminosity_constant)
print(gray_img_03[0, 0])  # [126.2]
