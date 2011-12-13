"""

Geotag clustering - clusters an array of images on geotag information

"""
from collections import defaultdict
from utility import gen_hex_color

DECIMALS = 2;

def parse_geotag_clusters(photos):
    """
    
    Parses out the geotag clusters from a passed in image array
    
    photos: The photo dictionary
    
    """ 
    clusters = cluster_photos(photos)
    return clusters

def cluster_photos(photos):
    """
    Clusters photos based on summation of their values
    
    photos: the photo dictionary
    
    """
     
    clusters = {}
    used_colors = {}
    count = 0
    
    #iterate photos, clustering by rounding the summation
    for photo in photos:
        rounded_sum = round(photo['coordsum'], DECIMALS)
        
        #if not in cluster, create entry and assign it a color
        if not rounded_sum in clusters:
            count += 1
            new_color = gen_hex_color(used_colors)
            used_colors[new_color] = new_color
            clusters[rounded_sum] = new_color;
            photo['iconcolor'] = new_color
        #otherwise, all same clusters get the same color
        else:
            photo['iconcolor'] = clusters[rounded_sum]
    print count
    return photos

# for testing purposes
if __name__ == "__main__":
    pass


