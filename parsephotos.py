"""

Main script for reading in images and parsing
out clusters based on passed in parameters

"""

#import the various cluster scripts
from cluster.geotag import parse_geotag_clusters
from cluster.color import parse_color_clusters
from cluster.date import parse_date_clusters
from cluster.tag import parse_tag_clusters


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
    
    #has additional information for geotag clustering
    if args is 'geotag':
        return parse_geotag_clusters(photos)
    elif args is 'color':
        clusters = parse_color_clusters(photos)
    elif args is'tag':
        clusters = parse_tag_clusters(photos)
    elif args is 'date':
        clusters = parse_date_clusters(photos)
    else:
        return None
    
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
    
    
    
    
    