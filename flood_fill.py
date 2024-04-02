# Author: Youssef AITBOUDDROUB

from PIL import Image 
import sys 
from collections import deque  # For using deque, a double-ended queue, to implement BFS
import os
import atexit  

def color_choice_to_rgb(choice):
    """
    Converts a numerical color choice into an RGB color value.

    Parameters:
    - choice (int): The numerical value representing the color.

    Returns:
    - tuple: An (R, G, B) tuple representing the corresponding color.
    """
    if choice == 0:
        return (0, 0, 0)  # Black
    elif choice == 1:
        return (255, 255, 255)  # White
    elif choice == 2:
        return (0, 255, 0)  # Green
    else:
        print("Invalid choice. Defaulting to Black.")
        return (0, 0, 0)  # Default to black if invalid choice

def create_image_matrix_from_file(file_path):
    """
    Reads a text file and converts it into a 2D list (matrix) representing an image.

    Parameters:
    - file_path (str): The path to the text file.

    Returns:
    - list of lists: A 2D list where each sublist represents a row in the image.
    """
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(value) for value in line.strip().split()]
            matrix.append(row)
    return matrix

def generate_image(matrix):
    """
    Generates an image from a 2D list (matrix) where each element represents a pixel's color.

    Parameters:
    - matrix (list of lists): The 2D list representing the image.

    Returns:
    - Image: The generated image.
    """
    rows, columns = len(matrix), len(matrix[0])
    image = Image.new('RGB', (columns, rows))  # Create a new RGB image
    for row in range(rows):
        for column in range(columns):
            # Set each pixel in the image according to the matrix
            image.putpixel((column, row), color_choice_to_rgb(matrix[row][column]))
    return image

def flood_fill(matrix, start_row, start_column, new_color):
    """
    Applies the flood fill algorithm to fill a contiguous area with a new color.

    Parameters:
    - matrix (list of lists): The image matrix.
    - start_row (int): The starting row for the fill.
    - start_column (int): The starting column for the fill.
    - new_color (int): The new color to apply.
    """
    rows, columns = len(matrix), len(matrix[0])
    original_color = matrix[start_row][start_column]
    if original_color == new_color:
        return  # Exit if the color is already the intended one

    queue = deque([(start_row, start_column)])  # Initialize queue with the start position

    while queue:
        row, column = queue.popleft()
        if matrix[row][column] == original_color:
            matrix[row][column] = new_color  # Fill with the new color
            # Enqueue neighboring cells if within bounds
            if row > 0:
                queue.append((row-1, column))
            if row < rows - 1:
                queue.append((row+1, column))
            if column > 0:
                queue.append((row, column-1))
            if column < columns - 1:
                queue.append((row, column+1))

def cleanup_images():
    """
    Removes specified image files upon script termination.
    """
    files_to_remove = ['zoomed_output_image.png', 'zoomed_output_image_updated.png']
    for file_path in files_to_remove:
        try:
            os.remove(file_path)
            print(f"Removed {file_path}")
        except OSError as e:
            print(f"Error: {file_path} : {e.strerror}")

def main(file_path):
    """
    The main function that orchestrates the reading, processing, and updating of the image based on user input.

    Parameters:
    - file_path (str): The path to the input file containing the image matrix.
    """
    matrix = create_image_matrix_from_file(file_path)  # Create the initial matrix from the file
    image = generate_image(matrix)  # Generate the initial image
    zoom_factor = 40  # Define the zoom factor for better visualization
    # Create and display a zoomed version of the initial image
    zoomed_image = image.resize((image.width * zoom_factor, image.height * zoom_factor), Image.NEAREST)
    zoomed_image.show()

    # Get user input for flood fill
    row, column, color = map(int, input("Enter row, column, and color (0 for black, 1 for white, 2 for green): ").split(','))

    # Validate the input coordinates
    if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]):
        print("Invalid pixel coordinates.")
        return
    
    # Apply flood fill and display the updated image
    flood_fill(matrix, row, column, color)
    image = generate_image(matrix)
    zoomed_image = image.resize((image.width * zoom_factor, image.height * zoom_factor), Image.NEAREST)
    zoomed_image.show()
    zoomed_image.save('zoomed_output_image_updated.png')  # Save the updated image

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python FloodFill.py image_matrix.txt")
        sys.exit(1)
    
    file_path = sys.argv[1]
    atexit.register(cleanup_images)  # Register the cleanup function to run at script termination
    main(file_path)  # Call the main function with the input file path
