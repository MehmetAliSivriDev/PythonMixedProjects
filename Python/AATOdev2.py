import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg


# Reading the original image, here 0 implies that image is read as grayscale
image = cv2.imread('lc.jpeg', 0)

# Generating the histogram of the original image
hist,bins = np.histogram(image.flatten(),256,[0,256])

# Generating the cumulative distribution function of the original image
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
 

 # Applying Histogram Equalization on the original image
image_equalized = cv2.equalizeHist(image)

# Generating the histogram of the equalized image
hist_equalized,bins_equalized = np.histogram(image_equalized.flatten(),256,[0,256])

# Generating the cumulative distribution function of the original image
cdf_equalized = hist_equalized.cumsum()
cdf_equalized_normalized = cdf_equalized * hist_equalized.max()/ cdf_equalized.max()

# Converting the image to YCrCb
image_yuv = cv2.cvtColor(image_c, cv2.COLOR_BGR2YUV)

# Applying Histogram Equalization on the original imageof the Y channel
image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:,:,0])

#Creating CLAHE 
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))

#Apply CLAHE to the original image
image_clahe = clahe.apply(image)


# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')
 

# Apply Min-Max Contrasting
min = np.min(image)
max = np.max(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)
