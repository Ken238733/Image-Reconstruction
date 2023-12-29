import cv2
import numpy as np
import matplotlib.pyplot as plt

original_paths = ["C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(64) through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(32) through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(16) through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(8) through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(4) through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(2) through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\(1) through midpoint.png"
    # List all paths for original images
]

inpainted_paths = ["C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(64) inpainted through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(32) inpainted through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(16) inpainted through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(8) inpainted through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(4) inpainted through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(2) inpainted through midpoint.png",
    "C:\\Users\\Ken23\\Documents\\lines through midpoint\\power of 2\\inpainted result\\(1) inpainted through midpoint.png"
    # List all paths for inpainted images
]

random_consecutive_lines_paths = ["C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^18.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^17.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^16.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^15.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^14.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^13.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^12.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^11.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^10.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^9.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^8.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^7.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^6.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^5.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^4.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^3.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^2.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^1.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\(modified) random line image 2^0.png",
    # List all paths for random consecutive lines images
]

random_consecutive_lines_inpainted_paths = ["C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^18.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^17.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^16.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^15.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^14.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^13.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^12.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^11.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^10.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^9.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^8.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^7.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^6.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^5.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^4.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^3.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^2.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^1.png",
"C:\\Users\\Ken23\\Documents\\modified random lines\\inpainted result\\inpainted random lines 2^0.png",

    # List all paths for random consecutive lines inpainted images
]

completely_random_lines_paths = [ "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^18.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^17.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^16.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^15.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^14.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^13.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^12.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^11.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^10.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^9.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^8.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^7.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^6.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^5.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^4.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^3.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^2.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^1.png",
                                  "C:\\Users\\Ken23\\Documents\\random lines\\random line image 2^0.png",]
completely_random_lines_inpainted_paths = [ "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^18.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^17.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^16.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^15.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^14.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^13.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^12.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^11.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^10.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^9.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^8.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^7.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^6.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^5.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^4.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^3.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^2.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^1.png",
                                            "C:\\Users\\Ken23\\Documents\\random lines\\inpainted results\\(random every time) inpainted random lines 2^0.png",]
vertical_lines_paths = [ "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png",
                        "C:\\Users\\Ken23\\Documents\\2^8 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^7 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^6 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^5 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^4 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^3 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^2 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^1 with two lines at the edges.png",
                         "C:\\Users\\Ken23\\Documents\\2^0 with two lines at the edges.png",]
vertical_lines_inpainted_paths = [ "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png", "C:\\Users\\Ken23\\Documents\\35.png",  "C:\\Users\\Ken23\\Documents\\inpainted_image (2^8).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^7).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^6).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^5).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^4).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^3).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^2).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^1).png",
                                    "C:\\Users\\Ken23\\Documents\\inpainted_image (2^0).png",
                                    ]


# Function to load images from a list of paths
def load_images(paths):
    images = []
    for path in paths:
        image = cv2.imread(path)
        if image is not None:
            images.append(image)
        else:
            print(f"Image at {path} not found or could not be loaded.")
            return None
    return images

# Load all sets of images
original_images = load_images(original_paths)
inpainted_images = load_images(inpainted_paths)
random_consecutive_lines_images = load_images(random_consecutive_lines_paths)
random_consecutive_lines_inpainted_images = load_images(random_consecutive_lines_inpainted_paths)
completely_random_lines_images = load_images(completely_random_lines_paths)
completely_random_lines_inpainted_images = load_images(completely_random_lines_inpainted_paths)
vertical_lines_images = load_images(vertical_lines_paths)
vertical_lines_inpainted_images = load_images(vertical_lines_inpainted_paths)

# Function to calculate Euclidean distances
def calculate_distances(images):
    num_images = len(images)
    distances = np.zeros((num_images, num_images))
    for i in range(num_images):
        for j in range(i, num_images):
            diff = np.square(images[i].astype(float) - images[j].astype(float))
            distance = np.sqrt(np.sum(diff))
            distances[i, j] = distances[j, i] = distance
    return distances / (512 * 512)  # Normalization

# Check if all image sets are loaded successfully
if all(images is not None for images in [
    original_images, inpainted_images,
    random_consecutive_lines_images, random_consecutive_lines_inpainted_images,
    completely_random_lines_images, completely_random_lines_inpainted_images,
    vertical_lines_images, vertical_lines_inpainted_images
]):

    # Calculate Euclidean distances for all sets of images
    original_distances = calculate_distances(original_images)
    inpainted_distances = calculate_distances(inpainted_images)
    random_consecutive_lines_distances = calculate_distances(random_consecutive_lines_images)
    random_consecutive_lines_inpainted_distances = calculate_distances(random_consecutive_lines_inpainted_images)
    completely_random_lines_distances = calculate_distances(completely_random_lines_images)
    completely_random_lines_inpainted_distances = calculate_distances(completely_random_lines_inpainted_images)
    vertical_lines_distances = calculate_distances(vertical_lines_images)
    vertical_lines_inpainted_distances = calculate_distances(vertical_lines_inpainted_images)

    # Create a list of image labels in the desired order
    image_labels = [f"s{i}" for i in range(18, -1, -1)]

    # Define markers, colors, and labels for each plot
    markers = ['o', 's', '^', 'D', 'v', '>', '<', 'p']  # Corrected markers
    colors = ['blue', 'red', 'brown', 'purple', 'green', 'orange', 'blueviolet', 'teal']
    labels = [
        'Case #1 Vertical lines', 'Case #1 Vertical lines (Inpainted)',
        'Case #2 Completely random lines', 'Case #2 Completely random lines (Inpainted)',
        'Case #3 Random consecutive lines', 'Case #3 Random consecutive lines (Inpainted)',
        'Case #4 Lines through midpoint', 'Case #4 Lines through midpoint (Inpainted)'
    ]

    # Plotting the Euclidean distances for all sets
    plt.figure()
    for distances, color, label, marker in zip(
            [vertical_lines_distances, vertical_lines_inpainted_distances,
             completely_random_lines_distances, completely_random_lines_inpainted_distances,
             random_consecutive_lines_distances, random_consecutive_lines_inpainted_distances,
             original_distances, inpainted_distances],
            colors, labels, markers):
        plt.plot(image_labels, distances[0], marker=marker, color=color, linestyle='-', label=label)

    plt.xlabel("s")
    plt.ylabel("Normalized Euclidean Distance")
    plt.title("Normalized Euclidean Distances from s18 to s0")
    plt.grid(True)


    plt.savefig('euclidean_distances_plot.png')  # Save the plot

    # Create and save the legend as a separate image
    fig_legend, ax_legend = plt.subplots()
    handles = [plt.Line2D([0], [0], color=colors[i], marker=markers[i], linestyle='-', label=labels[i])
               for i in range(len(labels))]
    legend = ax_legend.legend(handles=handles, loc='center')
    ax_legend.axis('off')
    fig_legend.canvas.draw()

    # Set the size of the saved legend image to match the drawn canvas
    bbox = legend.get_window_extent().transformed(fig_legend.dpi_scale_trans.inverted())
    fig_legend.savefig('legend.png', bbox_inches=bbox)

else:
    print("Failed to load all images.")