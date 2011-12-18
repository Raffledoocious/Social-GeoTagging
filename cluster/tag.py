"""

Tag clustering

"""
from utility import gen_hex_color

def build_tag_dict(photos):
    """
    Builds the tag dictionary
    """
    tags = {}
    
    #build tag dictionary
    for photo in photos:
        
        photo_tags = photo['tags'].split(' ')
        
        #update counts of all tags in the dictionary
        for tag in photo_tags:
            if not tag in tags:
                tags[tag] = {'count':1, 'color':None}
            else:
                tags[tag]['count'] += 1
        
    return tags
                
                
def assign_colors(photos, tags):
    """
    Assigns photo color to most common tag
    """
    used_colors = {}
    
    #assign color of photo to the color of the most related tag
    for photo in photos:
        min_count = len(photos) + 1
        photo_tags = photo['tags'].split(' ')
        
        #for photos with tag with search term, assign initially to first item
        best_tag = photo_tags[0]
        
        #find most common tag
        for tag in photo_tags:
            assoc_tag = tags[tag]
            
            #found a common tag, not including one common to all photos
            if assoc_tag['count'] < min_count:
                min_count = assoc_tag['count']
                best_tag = tag
        
        #generate a color for tag if it does not have one
        if tags[best_tag]['color'] is None:
            tags[best_tag]['color'] = gen_hex_color(used_colors)
        
        photo['iconcolor'] = tags[best_tag]['color']                 
                    

def parse_tag_clusters(photos):
    """
    Does analysis on image tags from images and clusters them
    """
    
    #dict holding tag maps to count and color for tag
    
    
    tags = build_tag_dict(photos)
    assign_colors(photos, tags)
    
    return photos                