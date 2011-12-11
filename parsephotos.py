"""

Main script for reading in images and parsing
out clusters based on passed in parameters

"""

#import the various cluster scripts
from cluster.geotag import parse_geotag_clusters


def parse_clusters(args, photos):
    """ 
    Parse out clusters based on the passed in arguments
    
    args: The parsin arguments to use
    photos: The photo array
        
    NOTE: args need to still be decided on
    """
    
    #here will have information to determine what kind of clusters are returned
    #for now just parses out geoTag information
    
    clusters = []
    
    clusters = parse_geotag_clusters(photos)
    
    return clusters
    
    
    
    


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
    
    
    
    
    