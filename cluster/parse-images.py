"""

Main script for reading in images and parsing
out clusters based on passed in parameters

"""
from PIL import Image
import color
import os

IMAGES_FOLDER = "..\images"
IMAGE_EXT = ".jpg"

def get_PIL_images():
    """
    Reads in the images from the images folder
    and copies into an array for parsing
    
    Returns: 
        A dict mapping image name to PIL libary ImageOpen variable
    """
    images = {}
    
    #loop of all .jpg image files
    for fn in os.listdir(IMAGES_FOLDER):
        if (fn.endswith('.jpg')): 
            file_path = IMAGES_FOLDER + "\\" + fn
            image = Image.open(file_path)
            images[file_path] = image
    return images



def parse_clusters(args):
    """ b bg
    Parse ou0 t clusters based on the passed in arguments
    
    NOTE: args need to still be decided on
    """
    images = get_PIL_images()
    
    #parse out args starting here, otherwise do tag parsing for now
    clusters = color.get_color_clusters(images)   




if __name__ == "__main__":
    """
    for testing purposes
    """
    
    """
    image_arr = os.listdir(IMAGES_FOLDER)
    if image_arr[0].endswith('.jpg'):
        print True
    """
    parse_clusters(None)
    
    
    
    
    