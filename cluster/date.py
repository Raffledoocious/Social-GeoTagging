'''
Parses out images based on date taken

@author: Jared
'''
from datetime import date, datetime

#need relative delta module
from dateutil.relativedelta import relativedelta

YEAR_COLOR = 'BBFF0000'
YEAR_SIX_MONTHS_COLOR = 'BB0033CC'
SIX_MONTHS_WEEK_COLOR = 'BBFF9D00'
WEEK_COLOR = 'BB33FF00'

def parse_date_clusters(photos):
    """
    Parses out images based on their date taken
    
    Currently puts photos into buckets of one year,
    six months, and seven days old
    
    """
    
    #get the times needed for clustering
    now = date.today()
    one_year = now - relativedelta(years =+ 1)
    six_months = now - relativedelta(months =+ 6)
    one_week = now - relativedelta(days =+ 7)
    
    #assign photo colors
    for photo in photos:
        date_str = photo['date'].split(' ')[0]
        photo_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                
        #if older than one year
        if photo_date <= one_year:
            photo['iconcolor'] = YEAR_COLOR
            
        #year to six months
        elif photo_date > one_year and photo_date <= six_months:
            photo['iconcolor'] = YEAR_SIX_MONTHS_COLOR
        
        #six months to week
        elif photo_date > six_months and photo_date <= one_week:
            photo['iconcolor'] = SIX_MONTHS_WEEK_COLOR
        
        #three months or less
        else:
            photo['iconcolor'] = WEEK_COLOR
    
    
    return photos