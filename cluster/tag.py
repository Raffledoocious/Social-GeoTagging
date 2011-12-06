"""

Tag clustering

"""

def getTags(img):
    """
    Gets the tags for a passed in Image
    """
    ret = {}
    info = img._getexif()
    print info
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def get_tag_clusters(images):
    """
    Does analysis on image tags from images and clusters them
    """
    
    pass