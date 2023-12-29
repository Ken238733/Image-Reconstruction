import cv2
import numpy as np
import matplotlib.pyplot as plt

def interpolate_zeros_with_midpoints(lst):
    interpolated_list = lst.copy()
    zero_runs = []
    current_run = []

    # Find zero runs in the list
    for i, num in enumerate(interpolated_list):
        if num == 0:
            current_run.append(i)
        elif current_run:
            zero_runs.append(current_run)
            current_run = []

    if current_run:
        zero_runs.append(current_run)

    # Interpolate zeros with midpoints
    for run in zero_runs:
        start_index = run[0]
        end_index = run[-1]
        start_value = lst[start_index - 1] if start_index > 0 else None
        end_value = lst[end_index + 1] if end_index < len(lst) - 1 else None

        # Linear interpolation
        if start_value is not None and end_value is not None:
            delta = np.int32(end_value) - np.int32(start_value)
            interpolated_values = [
                np.clip(int(np.int32(start_value) + delta * (i - start_index + 1) / (end_index - start_index + 2)), 0, 255)
                for i in run
            ]

            # Replace zeros with interpolated values
            for index, value in zip(run, interpolated_values):
                interpolated_list[index] = value

            # Calculate the midpoint index
            midpoint_index = start_index + (end_index - start_index) // 2
            interpolated_list[midpoint_index] = np.clip(int((np.int32(start_value) + np.int32(end_value)) // 2), 0, 255)

    return interpolated_list

# Read or create a synthetic image (replace 'your_image.jpg' with the path to your image)
# If you don't have an image, you can create a synthetic one using numpy:
# image = np.random.randint(0, 256, (512, 512), dtype=np.uint8)

image = cv2.imread('C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^18.png', cv2.IMREAD_GRAYSCALE)

# Flatten the image to a 1D array for interpolation
flat_image = image.flatten()

# Apply interpolation function to the flattened image
interpolated_values = interpolate_zeros_with_midpoints(flat_image)

# Reshape the interpolated values back to a 512x512 array
inpainted_image = np.array(interpolated_values).reshape(image.shape)

# Save the inpainted image
cv2.imwrite('C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^18.png', inpainted_image)

# Display the original and inpainted images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(inpainted_image, cmap='gray')
plt.title('Inpainted Image')

plt.show()
