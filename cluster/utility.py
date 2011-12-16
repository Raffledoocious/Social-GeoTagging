'''
Miscellaneous functions for clustering, parsing, image assignment, etc

@author: Jared

'''
import struct
import random

COLOR_MAX = 255

# according to this we can't color the white icon, need to be separate icons
# http://groups.google.com/group/kml-support-getting-started/browse_thread/thread/e41698f1fa94cfe0
def returnColor(color):
    if color=='red':
        return 'http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png'
    elif color=='blue':
        return 'http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png'
    elif color=='green':
        return 'http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png'
    elif color=='yellow':
        return 'http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'
    elif color=='purple':
        return 'http://maps.google.com/mapfiles/kml/pushpin/purple-pushpin.png'
    else:
        return 'http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png'

def rgb_to_hex(rgb_tuple):
    """
    
    Converts an rgb tuple to hex string
    
    """
    hex_color = 'ff%02x%02x%02x' % rgb_tuple
    return hex_color

def gen_hex_color(used_colors):
    """
    
    Generates a random hex color for assignment to cluster pins
    
    used_colors: A list of colors which have already been used
    
    """
    
    #generate color, keep generating until get one which is not assigned
    color_tuple = (random.randint(0, COLOR_MAX), random.randint(0,COLOR_MAX), random.randint(0,COLOR_MAX))
    while color_tuple in used_colors:
         color_tuple = (random.randint(0, COLOR_MAX), random.randint(0,COLOR_MAX), random.randint(0,COLOR_MAX))
         
    
    hex_color = rgb_to_hex(color_tuple)
    used_colors[hex_color] = hex_color
    #pack and return hex string
    return hex_color

