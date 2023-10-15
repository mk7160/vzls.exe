import os
from PIL import Image, ImageOps
from collections import Counter

def find_newest_image_in_folder(folder_path, extensions=['.jpg', '.jpeg', '.png']):
    files = os.listdir(folder_path)
    image_files = [f for f in files if any(f.lower().endswith(ext) for ext in extensions)]
    
    if not image_files:
        raise FileNotFoundError("No image files found in the specified folder.")
    
    newest_image = max(image_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    
    return os.path.join(folder_path, newest_image)

def find_prevalent_color(image):
    # Convert the image to RGB mode (in case it's in a different mode)
    image_rgb = image.convert('RGB')
    
    # Get all pixels from the image
    pixels = list(image_rgb.getdata())
    
    # Count the occurrence of each color in the image
    color_counts = Counter(pixels)
    
    # Get the most common color (prevalent color)
    prevalent_color = color_counts.most_common(1)[0][0]
    
    return prevalent_color

def auto_crop_to_square_with_prevalent_color(image_path, output_path):
    # Open the image using Pillow
    original_image = Image.open(image_path)
    
    # Determine the shorter dimension
    shorter_side = min(original_image.width, original_image.height)
    
    # Get the prevalent color in the image
    filler_color = find_prevalent_color(original_image)
    
    # Create a new image with the desired dimensions and the prevalent color as padding
    if original_image.width > original_image.height:
        new_image = Image.new('RGB', (original_image.width, original_image.width), filler_color)
        paste_position = (0, (original_image.width - original_image.height) // 2)
    else:
        new_image = Image.new('RGB', (original_image.height, original_image.height), filler_color)
        paste_position = ((original_image.height - original_image.width) // 2, 0)
    
    # Paste the original image onto the new image (adding padding)
    new_image.paste(original_image, paste_position)
    
    # Save the resulting image as a JPEG file
    new_image.save(output_path + ".jpg")  # Save as a JPEG image

# Example usage
folder_path = r"C:\Users\mike2\Desktop\vzls\imgs"  # Replace with the actual folder path
output_path = r"C:\Users\mike2\Desktop\vzls\crops\output_image"  # Replace with the desired output path

# Find the newest image in the folder
newest_image_path = find_newest_image_in_folder(folder_path)

# Perform auto cropping to square with prevalent color as padding
auto_crop_to_square_with_prevalent_color(newest_image_path, output_path)