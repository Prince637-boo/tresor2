from skimage import data
from skimage import color
import matplotlib.pyplot as plt

image = data.astronaut()  # image d'exemple sous forme de tableau NumPy
gray_image= color.rgb2gray(image)
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()