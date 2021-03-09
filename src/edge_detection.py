#!/usr/bin/env python

'''
Assignment 3
Finding text using edge detection

This script executes the following tasks:

- Draws a green rectangular box to show a region of interest (ROI) around the main body of text in the middle of the image. Saves this as image_with_ROI.jpg.
- Crops the original image to create a new image containing only the ROI in the rectangle. Saves this as image_cropped.jpg.
- Using this cropped image, uses Canny edge detection to 'find' every letter in the image
- Draws a green contour around each letter in the cropped image. Saves this as image_letters.jpg


'''

# Importing packages
import os
import sys
sys.path.append(os.path.join(".."))
import cv2
import numpy as np
import matplotlib.pyplot as plt


## Define main function
def main():
    # defining the path to image
    fname = os.path.join("data", "Edge_detection", "Memorial_IMG.jpg")
    # reading the image
    image = cv2.imread(fname)
    
    
## Drawing Region of Interest (ROI)

    ''' First, I find out the dimensions of the image so I know the scale and can decide what dimensions I should start with drawing the region of interest (see .ipynb file). Then, I set the start and end points for the x and y axis of the rectagle (ROI) by trial and error.
    #cv2.rectangle(image, start_point, end_point, color, thickness) '''      
    
    # drawing a rectangle ROI around the text
    image_ROI = cv2.rectangle(image, (1400, 880), (2855, 2800), (0, 225, 0), 6)       
    # defining the directory where to save the image with RIO
    output_path = os.path.join("data", "Edge_detection", "image_with_ROI.jpg")
    # saving the image with RIO
    cv2.imwrite(output_path, image_ROI)
    
    
    
## Cropping the image

    ''' To crop the image with ROI I used simple slicing with indexing '''

    # cropping the image
    image_cropped = image_ROI[880:2800, 1400:2855]
    # defining the directory where to save the cropped image
    output_path = os.path.join("data", "Edge_detection", "image_cropped.jpg")
    # saving the cropped image
    cv2.imwrite(output_path, image_cropped)
    
    
    
## Canny edge detection  

    ''' Using the cropped image, I am applying Canny edge detection to 'find' every letter in the image

    Steps:

    - Image turned into greyscale
    - Applied Gaussian Blur
    - Canny edge detection '''

    # making image greyscale for a better edge detection
    grey_image = cv2.cvtColor(image_cropped, cv2.COLOR_BGR2GRAY)
    # applying Gaussian Blur to remove the noise in the image
    blurred = cv2.GaussianBlur(grey_image, (5,5), 0)
    # canny edge detection with minVal and maxVal
    canny = cv2.Canny(blurred, 115, 160)
    
    ''' Here I experiment with two threshold values of cv2.Canny, minVal and maxVal, to reduce as much noise as possible while detecting as many letters as possible.
        Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to “sure-edge” pixels, they are considered to be part of edges. Otherwise, they are also discarded. '''
    
    
    
## Finding letters´ contours

    (contours, _) = cv2.findContours(canny.copy(), 
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                    )
    
    
    image_letters = cv2.drawContours(image_cropped.copy(), # draw contours on original cropped
                        contours,      # list of contours
                        -1,            # which contours to draw
                        (0, 255, 0),   # contour colour
                        2)           # contour pixel width
    
    
    # defining the directory where to save the cropped image
    output_path = os.path.join("data", "Edge_detection", "image_letters.jpg")
    # saving the cropped image
    cv2.imwrite(output_path, image_letters)

    
    
# Define behaviour when called from command line
if __name__=="__main__":
    main()
    
    print(f"Cool, it is done! Check 'data/Edge_detection' directory for the output images!")
    
 
    
    