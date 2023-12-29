# Corrected function for creating a 512x512 image with vertical lines, ensuring the edge lines are exactly on the edges
import numpy as np
import matplotlib.pyplot as plt
# Adjusting the function to draw the edge lines exactly at the coordinates specified:
# Line 1 from (0,0) to (0,512) and Line 2 from (512,0) to (512,512).

def create_vertical_lines_image_exact_edges(x):
    """
    Create a 512x512 image with two 1-pixel thick white vertical lines exactly at the edges:
    from (0,0) to (0,512) for the left edge and from (512,0) to (512,512) for the right edge.
    And 2^x white vertical lines in between.
    :param x: The exponent to determine the number of lines in between the edges.
    :return: A NumPy array representing the image.
    """
    # Number of lines is 2^x for the lines in between the edges
    total_lines = 2 ** x
    image_width = 512  # Adjusted image size
    line_color = (1, 1, 1)  # White color

    # Create an image with black background
    image = np.zeros((image_width, image_width, 3))

    # Draw the edge lines exactly at the coordinates (0,0) to (0,512) and (512,0) to (512,512)
    image[:, 0] = line_color  # Left edge line at (0,0) to (0,512)
    image[:, image_width-1] = line_color  # Right edge line at (512,0) to (512,512)

    # Calculate the positions for the in-between lines, excluding the very first and last columns for the edge lines
    spacing = image_width // (total_lines + 1)
    for i in range(1, total_lines + 1):
        position = spacing * i
        image[:, position] = line_color  # Line thickness of 1 pixel

    return image

# Generate and display the image with x = 3
image_512_exact_edges = create_vertical_lines_image_exact_edges(2)

# Display the image
plt.imshow(image_512_exact_edges)
plt.axis('off')  # Turn off the axis
plt.show()
