from PIL import Image
import random
import numpy as np

# Function definitions for the first part (Finding the maximum product run)
def find_max_product_run(image_pixels, image_width):
    max_product_run = None
    max_product = 0

    for i in range(len(image_pixels)):
        if image_pixels[i] == 0:
            run_length = 1
            while i + run_length < len(image_pixels) and image_pixels[i + run_length] == 0:
                run_length += 1

            left_value = image_pixels[i - 1] if i > 0 else 0
            right_value = image_pixels[i + run_length] if i + run_length < len(image_pixels) else 0
            slope = (right_value - left_value) / run_length
            product = abs(slope) * run_length

            mid_point_x = (i + i + run_length) // 2 % image_width
            mid_point_y = (i + i + run_length) // (2 * image_width)

            current_run = {
                'left_value': left_value,
                'right_value': right_value,
                'run_length': run_length,
                'slope': slope,
                'product': product,
                'mid_point': (mid_point_x, mid_point_y)
            }

            if product > max_product:
                max_product = product
                max_product_run = current_run

            i += run_length
        else:
            i += 1

    return max_product_run

# Function definitions for the second part (Finding the closest line)
def distance_from_line(point, line_point1, line_point2):
    x0, y0 = point
    x1, y1 = line_point1
    x2, y2 = line_point2
    return np.abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / np.sqrt((y2 - y1)**2 + (x2 - x1)**2)

def restrict_start_point_range(given_point, width, height):
    x_given, y_given = given_point
    min_x = max(0, x_given - y_given)
    max_x = min(width - 1, x_given + (height - y_given - 1))
    return min_x, max_x

def find_closest_line(start_point, given_point, width, height):
    min_distance = float('inf')
    closest_bottom_point = None

    for x_bottom in range(width):
        bottom_point = (x_bottom, height - 1)
        distance = distance_from_line(given_point, start_point, bottom_point)
        if distance < min_distance:
            min_distance = distance
            closest_bottom_point = bottom_point

    return start_point, closest_bottom_point

# Main logic to combine the functionalities
def calculate_and_find_line(image_path, width, height):
    # Open and process the image
    img = Image.open(image_path)
    img_gray = img.convert("L")
    image_pixels = list(img_gray.getdata())

    # Find the max product run
    max_product_run = find_max_product_run(image_pixels, width)

    if max_product_run:
        # Use the midpoint as the given point
        given_point = max_product_run['mid_point']

        # Restrict the start point range
        min_x, max_x = restrict_start_point_range(given_point, width, height)

        # Randomly select a start point
        start_point = (random.randint(min_x, max_x), 0)

        # Find the closest line
        top_row_point, bottom_row_point = find_closest_line(start_point, given_point, width, height)
        return top_row_point, bottom_row_point, given_point
    else:
        return None, None, None

# Example usage
image_path = "C:\\Users\\Ken23\\Documents\\lines through midpoint\\(74) through midpoint.png"
top_row_point, bottom_row_point, midpoint = calculate_and_find_line(image_path, 512, 512)

print("Top row point:", top_row_point)
print("Bottom row point:", bottom_row_point)
print("Midpoint of max product run:", midpoint)
