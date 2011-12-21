'''
Parses out images based on date taken

@author: Jared
'''
from datetime import date, datetime

#need relative delta module
from dateutil.relativedelta import relativedelta
from collections import defaultdict

YEAR_COLOR = 'BBFF0000'
YEAR_SIX_MONTHS_COLOR = 'BB0033CC'
SIX_MONTHS_WEEK_COLOR = 'BBFF9D00'
WEEK_COLOR = 'BB33FF00'

def write_results(cluster_dict):
    """
    Write out cluster results for user
    """
    
    f = open('cluster\date_date.txt', 'w')
    f.write('Date Cluster Information \n\n')
    
    now = date.today()
    now = datetime.strftime(now, '%m-%d-%y')
    #write out information for reach cluster
    f.write('Photos older than a year from: ' + now + '\n')
    f.write('Color: ' + YEAR_COLOR + '\n\n')
    list = cluster_dict[YEAR_COLOR]
    for photo in list:
        f.write(photo['title'] + '\n')
    f.write('\n\n')
    
    f.write('Photos between a year and six months from: ' + now + '\n')
    f.write('Color: ' + YEAR_SIX_MONTHS_COLOR + '\n\n')
    list = cluster_dict[YEAR_SIX_MONTHS_COLOR]
    for photo in list:
        f.write(photo['title'] + '\n')
    f.write('\n\n')
    
    f.write('Photos between six months and a week from: ' + now + '\n')
    f.write('Color: ' + SIX_MONTHS_WEEK_COLOR + '\n\n')
    list = cluster_dict[SIX_MONTHS_WEEK_COLOR]
    for photo in list:
        f.write(photo['title'] + '\n')
    f.write('\n\n')
    
    f.write('Photos less than a week old from: ' + now + '\n')
    f.write('Color: ' + WEEK_COLOR + '\n\n')
    list = cluster_dict[WEEK_COLOR]
    for photo in list:
        f.write(photo['title'] + '\n')
    
    f.close()
        

def parse_date_clusters(photos):
    """
    Parses out images based on their date taken
    
    Currently puts photos into buckets of one year,
    six months, and seven days old
    
    """
    #dict for writing out user information
    cluster_dict = defaultdict(list)
    
    
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
            cluster_dict[YEAR_COLOR].append(photo)
            
        #year to six months
        elif photo_date > one_year and photo_date <= six_months:
            photo['iconcolor'] = YEAR_SIX_MONTHS_COLOR
            cluster_dict[YEAR_SIX_MONTHS_COLOR].append(photo)
            
        #six months to week
        elif photo_date > six_months and photo_date <= one_week:
            photo['iconcolor'] = SIX_MONTHS_WEEK_COLOR
            cluster_dict[SIX_MONTHS_WEEK_COLOR].append(photo)
            
        #three months or less
        else:
            photo['iconcolor'] = WEEK_COLOR
            cluster_dict[WEEK_COLOR].append(photo)
            
        write_results(cluster_dict)
    
    return photos