"""
Clusters photos based on the color assigning a relative color for the pin

"""
import utility
from PIL import Image
import math
from collections import defaultdict

def average_color(photo):
    """
    Gets the average color within a photo
    """
    
    i = Image.open(photo['file'])
    colors = i.getcolors(1024*1024)
    
    r = 0
    g = 0
    b = 0
    
    r_count = 0
    g_count = 0
    b_count = 0
    
    #iterate over all parsed out colors
    for color in colors:
        r += (color[1][0] * color[0])
        r_count += color[0]
        g += (color[1][1] * color[0])
        g_count += color[0]
        b += (color[1][2] * color[0])
        b_count += color[0]
    
    #compute the averages
    r = int(math.floor(r / r_count))
    g = int(math.floor(g / g_count))
    b = int(math.floor(b / b_count))
    
    #create and return color tuple
    rgb_tuple = r,g,b
    return rgb_tuple       
    
def most_common_color(photo):
    """
    Sets the most common color as the image
    """
    
    most_common = 0
    index = 0
    
    i = Image.open(photo['file'])
    colors = i.getcolors(1024*1024)
    
    for i in range(0, len(colors)):
        color = colors[i]
        count = color[0]
        if count > most_common:
            most_common = count
            index = i
    
    return colors[index][1]

def append_color_pin(photo):
    """
    Assigns the pin color based on image
    """
    
    #color = average_color(photo)
    color = most_common_color(photo)
    color_hex = utility.rgb_to_hex(color)
    
    photo['iconcolor'] = color_hex
    
    return photo

def write_results(cluster_dict):
    """
    Prints out the final cluster data for use by user
    """
    f = open('cluster\color_data.txt', 'w')
    
    f.write('Color Cluster Information \n\n')
    
    for key in cluster_dict.keys():
        f.write('Photos with color: ' + key + '\n')
        list = cluster_dict[key]
        for photo in list:
            f.write(photo['title'] + '\n')
        f.write('\n\n')
    f.close()
    
def parse_color_clusters(photos):
    """
    Parses out photo clusters
    """
    #dict which holds the final photo clusters for printint out data
    
    cluster_dict = defaultdict(list)
    
    for photo in photos:
        photo = append_color_pin(photo)
        cluster_dict[photo['iconcolor']].append(photo)
    
    write_results(cluster_dict)
        
        
    return photos