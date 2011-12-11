"""

Geotag clustering - clusters an array of images on geotag information

"""
from collections import defaultdict

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
    
    clusters = defaultdict(list)
    
    #iterate photos, clustering by rounding the summation
    for photo in photos:
        rounded_sum = round(photo['coordsum'], DECIMALS)
        clusters[rounded_sum].append(photo)  
    
    return clusters   

# for testing purposes
if __name__ == "__main__":
    pass


