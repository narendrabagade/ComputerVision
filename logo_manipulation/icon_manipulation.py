import cv2
import numpy as np

# Read the image of a yellow square ('yellow_square.png')
img_yellow_square = cv2.imread('yellow_square.png', cv2.IMREAD_COLOR)

# Read the image of a green/gray circle inside square.
img_green_circle = cv2.imread('green_circle.png', cv2.IMREAD_COLOR)

print('yellow square: ', img_yellow_square.shape)
print('gray circle:   ', img_green_circle.shape)

# Display image
cv2.imshow('img_yellow_square', img_yellow_square)
cv2.imshow('img_green_circle', img_green_circle)
cv2.waitKey(0)

# Resize background image according to FG image.
# Set the dimension of the background image to be the same as the logo.
logo_h = img_green_circle.shape[0]
logo_w = img_green_circle.shape[1]
dim = (logo_w, logo_h)

# Resize the yellow square.
img_yellow_square = cv2.resize(img_yellow_square, dim, interpolation=cv2.INTER_AREA)

# Print the image sizes to confirm the width and height match.
print('yellow square: ', img_yellow_square.shape)
print('gray circle: ', img_green_circle.shape)

# Display.
cv2.imshow('Foreground', img_green_circle)
cv2.imshow('Background', img_yellow_square)
cv2.waitKey(0)

# Convert the green circle image to grayscale using cvtColor()
img_logo_gray = cv2.cvtColor(img_green_circle, cv2.COLOR_RGB2GRAY)
cv2.imshow('img_logo_gray', img_logo_gray)
cv2.waitKey(0)

# Use the threshold() function to create a binary mask (white RING inside a black square).
# Apply global thresholding to create a binary mask of the logo.
retval, img_ring_mask = cv2.threshold(img_logo_gray, 127, 255, cv2.THRESH_BINARY)
# Display.
cv2.imshow('img_ring_mask', img_ring_mask)
cv2.waitKey(0)

# Use the bitwise_not() function to create an inverse mask.
img_logo_mask_inv = cv2.bitwise_not(img_ring_mask)
cv2.imshow('img_logo_mask_inv', img_logo_mask_inv)
cv2.waitKey(0)


# Use bitwise_and() to create the final combined image (black ring on a yellow square)
# img_combined =
# Add the foreground and background.
img_combined = cv2.bitwise_and(img_yellow_square, img_yellow_square, mask = img_logo_mask_inv)
cv2.imshow('combined final', img_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()