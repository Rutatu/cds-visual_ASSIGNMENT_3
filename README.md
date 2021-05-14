# cds-visual_analytics_Assignment_3

***Assignment for visual analytics class at Aarhus University.***

***2021-03-08***


# Finding text using edge detection

## About the script

This assignment is Class Assignment 3. The task was to use computer vision to extract language-like objects, such as letters and punctuation from the image. To accomplish this task several operations had to be made: drawing region of interest, cropping the image, contouring letters.

## Methods

The problem of the task relates to detecting letters in an image using computer vision. To address this problem, firstly, I drew a green rectangular box to show a region of interest (ROI) around the main body of text in the middle of the image and saved this as image_with_ROI.jpg. Secondly, using simple slicing with indexing I cropped the original image to create a new image containing only the ROI in the rectangle and saved this as image_cropped.jpg. Thirdly, using this cropped image, I used Canny edge detection to 'find' every letter in the image. The following steps were executed: image turned into grayscale, applied Gaussian Blur, applied Canny edge detection. I experimented with two threshold values of ```cv2.Canny```: minVal and maxVal, to reduce as much noise as possible while detecting as many letters as possible. The image was saved as image_canny.jpg. Lastly, I drew a green contour around each letter in the cropped image and saved this as image_letters.jpg.


## Repository contents

| File | Description |
| --- | --- |
| data/ | Folder containing files produced by the scripts |
| data/Memorial_IMG.jpg | Input image for the script |
| data/image_with_ROI.jpg | Output Image with drawn region of interest |
| data/image_cropped.jpg | Output image cropped |
| data/image_canny.jpg | Output image with applied canny edge detection algorithm |
| data/image_letters.jpg | Output image with contoured letters|
| src/| Folder containing the script |
| src/edge_detection.py | The script of this project |
| edge_detection.sh | bash file for creating a virtual environmment |
| kill_edge_detection.sh | bash file for removing a virtual environment |
| README.md | Description of the assignment and the instructions |
| requirements.txt | list of python packages required to run the script |


## Data

For this task only one image in a JPG format was used. Image can be downloaded at the link below:

https://upload.wikimedia.org/wikipedia/commons/f/f4/%22We_Hold_These_Truths%22_at_Jefferson_Memorial_IMG_4729.JPG


## Intructions to run the codes

Code was tested on an HP computer with Windows 10 operating system. It was executed on Jupyter worker02.

__Steps__

Set-up:
```
#1 Open terminal on worker02 or locally
#2 Navigate to the environment where you want to clone this repository
#3 Clone the repository
$ git clone https://github.com/Rutatu/cds-visual_analytics_Assignment_3.git 

#4 Navigate to the newly cloned repo
$ cd cds-visual_analytics_Assignment_3

#5 Create virtual environment with its dependencies (and activate it)
$ bash edge_detection.sh
## $ source ./classification/bin/activate

``` 

Run the code:

```
#6 Navigate to the directory of the script
$ cd src

#7 Run the code
$ python edge_detection.py

#8 To remove the newly created virtual environment
$ bash kill_edge_detection.sh

 ```

I hope it worked!


## Results

Detecting letters in an image might seem trivial to us humans due to our visual system running the show behind the scenes. However, it is a tricky task for the computer. This task has proven that it is a challenge to detect each letter in one specific image detecting as little background noise as possible, let alone to automate such a task with many different images. In the output image called image_letters.jpg we can see that the inside contours of letters O and D were not detected. More experimenting with minVal and maxVal values of ```cv2.Canny```, which determine what is considered to be an edge or non-edge, might be necessary in order to improve the final result. Different preprocessing steps and blurring techniques might be considered as well.

