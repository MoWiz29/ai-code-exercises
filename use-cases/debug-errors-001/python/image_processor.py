# image_processor.py
import numpy as np
from PIL import Image
import os

def load_and_process(image_path):
    # Load the image
    img = Image.open(image_path)

     # Resize to something manageable
    img = img.resize((500, 500))

    # Convert image to a small NumPy array
    image_data = np.array(img, dtype=np.uint8)

    img.close()

    return image_data
def process_images(image_files):

    for image_file in image_files:
          yield load_and_process(image_file)
       

def main():
    # Get list of image files
    image_directory = "sample_images"
    image_files = [
        os.path.join(image_directory, f)
        for f in os.listdir(image_directory)
        if f.endswith('.jpg')
    ]

    count = 0

    for image_data in process_images(image_files):
        # Save/display/process image here
        count += 1

        del image_data  # release memory

    print(f"Processed {count} images")
