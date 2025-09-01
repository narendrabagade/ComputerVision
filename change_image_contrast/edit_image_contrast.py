import cv2
import numpy as np

# Read and display original image.
image = 'Santorini.jpg'
img = cv2.imread(image, cv2.IMREAD_COLOR)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create a matrix of ones (with data type float64)
matrix_ones = np.ones(img.shape,dtype='float64')

# Create two higher contrast images using the 'scale' option with factors of 1.1 and 1.2 (without overflow fix)
img_lower   = np.uint8(cv2.multiply(np.float64(img), matrix_ones, scale = 1.1))
img_higher  = np.uint8(cv2.multiply(np.float64(img), matrix_ones, scale = 1.2))

# Display the images (original, higher (1.1x) , high (1.2x))
cv2.imshow('higher 1.1x', img_lower)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('higher 1.2x', img_higher)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Create higher contrast images using scale factors of 1.1 and 1.2 (using np.clip() to clip high values to 255)

img_lower  = np.uint8(np.clip(cv2.multiply(np.float64(img), matrix_ones, scale = 1.1) , 0, 255))
img_higher  = np.uint8(np.clip(cv2.multiply(np.float64(img), matrix_ones, scale = 1.2) , 0, 255))

cv2.imshow('Higher (1.1x): clipped', img_lower)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Higher (1.2x): clipped', img_higher)
cv2.waitKey(0)
cv2.destroyAllWindows()