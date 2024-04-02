# Flood Fill Project

## Overview

This project implements the classic flood fill algorithm in Python, using it to manipulate and transform images represented as matrices of pixel values. The flood fill algorithm, also known as seed fill, is an algorithm that determines the area connected to a given node in a multi-dimensional array and changes its color. This project consists of two main scripts: one for generating a random binary image matrix (generate_matrix.py) and the other for applying the flood fill algorithm on this matrix (flood_fill.py).

## Prerequisites

Python 3.x
Pillow (Python Imaging Library Fork)
Before running the project, ensure Python 3.x is installed on your system. You can download it from the official Python website. Additionally, you need the Pillow library for image processing tasks, which can be installed using pip:

pip install Pillow
## Project Structure

The project is structured into two main scripts:

* generate_matrix.py: This script generates a text file containing a random binary (0s and 1s) image matrix. The size of the matrix is predefined but can be adjusted by modifying the rows and columns variables within the script.
* flood_fill.py: This script reads the generated matrix from the text file, converts it into an image, and applies the flood fill algorithm based on user input. The user is prompted to enter the starting coordinates for the fill and the new color value. The script showcases the initial and transformed images, demonstrating the effect of the flood fill operation.
1. generate_matrix.py
This script automatically creates a text file named image_matrix.txt, containing a randomly generated matrix of 0s and 1s. The default size of the matrix is 380x380, but it can be adjusted by changing the rows and columns variables. The generated file serves as input for the flood fill script.

2. flood_fill.py
The core of the project, flood_fill.py, reads the matrix from image_matrix.txt, translates it into an image using the Pillow library, and visually displays the transformation caused by the flood fill algorithm. It also includes functionalities such as:

* Translating numerical color choices to RGB values for image manipulation.
* Creating an image from the matrix.
* Applying the flood fill algorithm using breadth-first search (BFS).
* Cleaning up generated images upon program termination.
## Usage

1. Generate the image matrix by running:

python generate_matrix.py
This will create image_matrix.txt in the current directory.
2. Run the flood fill script, passing the path to the generated matrix file as an argument:

python flood_fill.py image_matrix.txt
Follow the prompts to enter the starting coordinates for the flood fill and the color to apply.
View the initial and transformed images, which are displayed automatically by the script. The transformed image is also saved as zoomed_output_image_updated.png.
## Cleanup
 
The flood_fill.py script is designed to clean up generated image files (zoomed_output_image.png and zoomed_output_image_updated.png) upon termination, ensuring no residual files are left over after running the project.

## License

This project is open-sourced under the [MIT license](https://en.wikipedia.org/wiki/MIT_License). Feel free to fork, modify, and use it in your own projects.

## Acknowledgments

Youssef AITBOUDDROUB, for the initial creation and contribution to the project.
The Python and Pillow communities, for the excellent documentation and resources that made this project possible.
**Enjoy exploring and expanding the project!**