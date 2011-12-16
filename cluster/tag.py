"""

Tag clustering

"""
import pyexiv2

def getTags(img):
    """
    Gets the tags for a passed in Image
    """
    

def parse_tag_clusters(photos):
    """
    Does analysis on image tags from images and clusters them
    """
    
    #dict holding tag, count, and color associated with tag
    tags = {}
    used_colors = {}
    
    for photo in photos:
        #get the datetime and parse out the photo
        metadata = pyexiv2.ImageMetadata(photo['file'])
        metadata.read()
        print metadata.exif_keys()
    pass