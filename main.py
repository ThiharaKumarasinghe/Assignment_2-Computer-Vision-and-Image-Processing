# Name    : Kumarasinghe K.A.G.T.V
# Reg No. : EG/2019/3645

import numpy as np
import cv2 as cv

# Create a black background for the image
background = np.zeros((450, 450), dtype=np.uint8)

# Coordinates of the two object --> (x, y, width, height)
object1 = (50, 50, 150, 200)
object2 = (220, 220, 180, 140)

# Draw the objects on the background
cv.rectangle(background, (object1[0], object1[1]), (object1[0]+object1[2], object1[1]+object1[3]), 255, -1)
cv.rectangle(background, (object2[0], object2[1]), (object2[0]+object2[2], object2[1]+object2[3]), 150, -1)

# Define the image
img = background





# Display the image
cv.imshow('Image with Objects', img)
cv.waitKey(0)
cv.destroyAllWindows()