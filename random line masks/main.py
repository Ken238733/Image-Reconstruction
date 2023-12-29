import cv2
import random

def add_random_lines(image, num_random_lines):
    # Copy the original image to avoid modifying it directly
    result_image = image.copy()

    # Get the height and width of the image
    height, width, _ = image.shape

    # Add random lines from top to bottom
    for _ in range(num_random_lines):
        # Calculate the endpoint coordinates
        x1 = random.randint(0, width)
        y1 = 0  # Starting point at the topmost row of the image
        x2 = random.randint(0, width)
        y2 = height - 1  # Ending point at the bottommost row of the image

        # Draw the line on the result image
        result_image = cv2.line(result_image, (x1, y1), (x2, y2), (255, 255, 255), 1)

    return result_image

def main():
    image_path = 'C:\\Users\\Ken23\\PycharmProjects\\pythonProject11\\modified_image131072.png'
    num_random_lines = 131072

    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is not None:
        result_image = add_random_lines(image, num_random_lines)

        # Display the original and modified images
        cv2.imshow('Original Image', image)
        cv2.imshow('Modified Image', result_image)

        # Save the modified image
        cv2.imwrite('C:\\Users\\Ken23\\PycharmProjects\\pythonProject11\\modified_image262144.png', result_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('Failed to load the image.')

if __name__ == "__main__":
    main()
