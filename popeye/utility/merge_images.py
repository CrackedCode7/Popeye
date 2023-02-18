from PIL import Image
import json
import os


def merge_images(images: list, image_filename: str, texture_map_filename: str, scale: float=1) -> None:
    """Takes a list of image filenames and writes them out to a file"""

    # Initialize result image height and width to zero
    image_width = 0
    image_height = 0

    image_data = []

    for i in range(len(images)):

        # Open image, get the height and width, add data to list
        img = Image.open(images[i])
        width, height = img.size
        if scale != 1:
            img = img.resize(( int(scale*width), int(scale*height) ))
            width, height = img.size
        image_data.append(img)

        # Increment image width
        image_width += width

        # Re-size image height if too small to fit current image
        if height > image_height:
            image_height = height
    
    # Create image
    image = Image.new('RGBA', (image_width, image_height))

    current_width = 0
    texture_map = {}
    for i in range(len(image_data)):
        
        image.paste(im=image_data[i], box=(current_width, 0))
        texture_name = os.path.splitext(os.path.basename(images[i]))[0]
        texture_map[texture_name] = [current_width / image_width, (current_width+image_data[i].size[0]) / image_width, 0, 1]
        current_width += image_data[i].size[0]
        
    image.save(image_filename)
    with open(texture_map_filename, 'w') as f:
        json.dump(texture_map, f, indent=4)

    return