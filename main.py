# Name    : Kumarasinghe K.A.G.T.V
# Reg No. : EG/2019/3645

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt



# Generate function for adding gaussian noise
def addGaussianNoise(image, mean=0, sigma=25):
    # Generate a noise shape with original image dimensions
    gauss = np.random.normal(mean, sigma, image.shape)
    # Combine original image with noise
    noisyImage = np.clip(image + gauss, 0, 255)
    return noisyImage.astype(np.uint8),gauss


# Create a black background for the image
background = np.zeros((450, 450), dtype=np.uint8)

# Coordinates of the two object --> (x, y, width, height)
object1 = (50, 50, 150, 200)
object2 = (220, 220, 180, 140)

# Draw the objects on the background
cv.rectangle(background, (object1[0], object1[1]), (object1[0] + object1[2], object1[1] + object1[3]), 255, -1)
cv.rectangle(background, (object2[0], object2[1]), (object2[0] + object2[2], object2[1] + object2[3]), 150, -1)

# Define the image
img = background

# Add Gaussian noise to the image
gaussianNoiseImage, noise = addGaussianNoise(img)

# Create a subplot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Display the images
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(noise, cmap='gray')
axes[1].set_title('Noisy Image')
axes[1].axis('off')

axes[2].imshow(gaussianNoiseImage, cmap='gray')
axes[2].set_title('Image + Noise')
axes[2].axis('off')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()


