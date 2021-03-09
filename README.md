# cds-visual_analytics_Assignment_3

***Assignment for visual analytics class at Aarhus University.***

***2021-03-08***


# Finding text using edge detection

The purpose of this assignment is to use computer vision to extract specific features from images. In particular, the script is designed to find text, language-like objects, such as letters and punctuation. It includes such image processing methods as drawing region of interest, croping an image, canny edge detection and finding countours of objects.

# Instructions to run the code:

This repository is a subset taken from cds-visual environment on worker02. The 'data' folder contains 'Edge_detection' folder where the original picture 'Memorial_IMG' is located. The output files will end up in this folder after executing the code. There is a bash file edge_detection.sh for creating the environment with its dependencies and running the script and kill_edge_detection.sh file for removing the environment.A notebook (.ipynb) file was zipped due to its large size.  

Here are the instructions for runing this script using bash file in terminal on worker02:

##1 Preparation     
   - Create Edge_detection folder in data folder in cds-visual environment on worker02 and place there 'Memorial_IMG' image. 
   - Place edge_detection.py file in 'src' folder.
   - Place edge_detection.sh and kill_edge_detection.sh files in cds-visual environment
   - Place requirements.txt file in cds-visual environment
   
    ALTERNATIVELY
    
   - You could clone the repository, type: git clone https://github.com/Rutatu/cds-visual_analytics_Assignment_3.git. But I am unsure whether the script will succeed, I haven´t checked that.
    
##2 Execute the script
   - Open terminal
   - Navigate to the right environment, type: cd cds-visual  
   - Type: bash edge_detection.sh (this will install the requirements and will execute the script. In the end, you should get a message that it worked.)
   - Take a look at the folder 'Edge_detection' for the output files to make sure that the script worked.
   - To remove the newly created edge_detection environment type: bash kill_edge_detection.sh

I hope it worked :)
