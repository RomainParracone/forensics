# Forensics project

Goal of the project : making a command-line tool to detect edited images

A few ideas :
* Focusing on jpeg images only might be a good idea (most of the pictures are jpeg anyway). We might focus on one software as well (Adobe Photoshop ?).
* Check the exif data from jpeg images.
* Try to detect one or two specific attacks such as copy/paste attack.

### Work of Virgile on 05/27

Created dct_histo.py : it needs numpy, scipy and matplotlib to run. Take a 'clean' and picture and copy/paste another picture in it.  Put the  2 pictures in the current folder one named 'clean.jpeg' and the other 'tamper.jpeg', then run the script. It computes the blocks dct coefficients of the pixels of each picture and saves the results in the current folder. It also displays the gray scale images to check if they are well open. The goal is to try to see (visually) the differences in the blocks dct of the 2 pictures. NB : it is not optimized at all and may take some time to run. 
#### Deadline : 25/06/2018
