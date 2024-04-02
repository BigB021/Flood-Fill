# Author : Youssef AITBOUDDROUB

import random

# Size of the matrix
rows = 380
columns = 380

# Open a file in write mode
with open('image_matrix.txt', 'w') as file:
    for _ in range(rows):
        # Generate a row of random 0s and 1s
        row = ' '.join(str(random.randint(0, 1)) for _ in range(columns))
        # Write the row to the file
        file.write(row + '\n')

print(f"Generated a {rows}x{columns} image matrix and saved to 'image_matrix.txt'")
