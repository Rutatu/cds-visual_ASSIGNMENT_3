#!/usr/bin/env python

''' ---------------- About the script ----------------

Assignment 3: Finding text using edge detection

This script uses computer vision to extract language-like objects, such as letters and punctuation from the image. To accomplish this task several operations are executed: drawing region of interest, cropping the image, using Canny edge detection to 'find' every letter, contouring letters. After each operation the script saves a .jpg image in the data folder.

Example:    
    $ python edge_detection.py
        

'''



"""---------------- Importing libraries ----------------
"""

import os
import sys
sys.path.append(os.path.join(".."))
import cv2
import numpy as np
import matplotlib.pyplot as plt




"""---------------- Main script ----------------
"""

def main():
    # Defining the path to image
    im_name = os.path.join("..", "data", "Memorial_IMG.jpg")
    # Reading the image
    image = cv2.imread(im_name)
    
    
    
    
    """------ Drawing Region of Interest (ROI) ------
    
    First, I find out the dimensions of the image so I know the scale and can decide what dimensions I should start with drawing the region 
    of interest. Then, I set the start and end points for the x and y axis of the rectagle (ROI) by trial and error.
    I use this command: cv2.rectangle(image, start_point, end_point, color, thickness)
    
    
    """
    
    # Drawing a rectangle ROI around the text
    image_ROI = cv2.rectangle(image, (1400, 880), (2855, 2800), (0, 225, 0), 6)       
    # Defining the directory where to save the image with RIO
    output_path_ROI = os.path.join("..", "data", "image_with_ROI.jpg")
    # Saving the image with RIO
    cv2.imwrite(output_path_ROI, image_ROI)
    # Printing that .jpg file has been saved
    print(f"\n[INFO] Image with ROI is saved in directory {output_path_ROI}")
    
    
    
    """------ Cropping the image within ROI ------
    
    To crop the image part within ROI I used simple slicing with indexing
    
    """
    
    # Cropping the image
    image_cropped = image_ROI[880:2800, 1400:2855]
    # Defining the directory where to save the cropped image
    output_path_cropped = os.path.join("..", "data", "image_cropped.jpg")
    # Saving the cropped image
    cv2.imwrite(output_path_cropped, image_cropped)
    # Printing that .jpg file has been saved
    print(f"\n[INFO] Cropped image within ROI is saved in directory {output_path_cropped}")
    
    
    
    
    """------ Canny edge detection ------
    
    Using the cropped image, I am applying Canny edge detection to 'find' every letter in the image

    Steps:

    - Image turned into greyscale
    - Applied Gaussian Blur
    - Applied Canny edge detection 
    
    """    
    
    # Making image greyscale for a better edge detection
    grey_image = cv2.cvtColor(image_cropped, cv2.COLOR_BGR2GRAY)
    # Appplying Gaussian Blur to remove the noise in the image
    blurred = cv2.GaussianBlur(grey_image, (5,5), 0)
    # Canny edge detection with minVal and maxVal
    canny = cv2.Canny(blurred, 115, 160)
    
    '''
    Above I experiment with two threshold values of cv2.Canny: minVal and maxVal, to reduce as much noise as possible while detecting as 
    many letters as possible.
    Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so 
    discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they 
    are connected to “sure-edge” pixels, they are considered to be part of edges. Otherwise, they are also discarded. '''
    
    # Defining the directory where to save the image after I applied canny edge detection
    output_path_canny = os.path.join("..", "data", "image_canny.jpg")
    # Saving the image
    cv2.imwrite(output_path_canny, canny)
    # Printing that .jpg file has been saved
    print(f"\n[INFO] Image with applied canny edge detection is saved in directory {output_path_canny}")
    
    



    """------ Finding letters´ contours ------
    
    Here I draw green contours around each detected letter

    
    """  

    # Using cv2.findContours to find all the contours from the canny image
    (contours, _) = cv2.findContours(canny.copy(), # using a copy rather than an original image
                    cv2.RETR_EXTERNAL, # taking only the external structures and not for e.g. the edges within each coin
                    cv2.CHAIN_APPROX_SIMPLE # approximated contours
                    )
    
    # Original cropped image overlayed with contours
    image_letters = cv2.drawContours(image_cropped.copy(), # draw contours on original cropped
                        contours,      # list of contours
                        -1,            # which contours to draw
                        (0, 255, 0),   # contour colour
                        2)             # contour pixel width
    
    
    # Defining the directory where to save the contoured image
    output_path_contour = os.path.join("..", "data", "image_letters.jpg")
    # saving the cropped image
    cv2.imwrite(output_path_contour, image_letters)
    # Printing that .jpg file has been saved
    print(f"\n[INFO] Contoured image is saved in directory {output_path_contour}")
    
    
    # Final message to the user
    print(f"Success, the script was executed! Check 'data' folder for the output images!")

    
    
# Define behaviour when called from command line
if __name__=="__main__":
    main()
    
    
    
 
    
    