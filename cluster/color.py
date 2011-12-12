"""
Clusters photos based on the color assigning a relative color for the pin

"""
from utility import returnColor
from PIL import Image


def get_color(color_tuple):
    """
    
    Takes a color tuple and converts it to a string array
    
    """
    
def append_color_pin(photo):
    """
    
    Assigns the pin color based on image
    
    """
    color_dict = {'yellow':0, 'red':0, 'blue':0, 'green':0, 'orange':0, 'purple':0}
    
    pil_image = Image.open(photo['file'])
    colors = pil_image.getcolors(256)
    for color in colors:
        count = color[0]
        color_tuple = color[1]
        
        assigned_color = get_color(color_tuple)
        
        if assigned_color is not None:
            color_dict[assigned_color] += count
        
        
        x = 10
    return None
    
def parse_color_clusters(photos):
    
    pil_images = []
    
    for photo in photos:
        append_color_pin(photo)
        
    return None