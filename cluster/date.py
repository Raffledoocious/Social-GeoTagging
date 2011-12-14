'''
Parses out images based on date taken

@author: Jared
'''

from datetime import date

YEAR_OFFSET = 12
HALF_YEAR = 6
WEEK = 7


def parse_date_clusters(photos):
    """
    Main parsing algorithm
        
    """
    for photo in photos:
        #get the datetime and parse out the photo
        photo['time'] = date.today()
        
        #if > year old
        
        #if < year but > 6mo
        
        #if < week
        
        
    return photos

    
