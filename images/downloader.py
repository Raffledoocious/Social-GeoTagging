import flickrapi
import urllib, urlparse
import os
import sys

def write_info(info, dateslist, tagslist):
    """
    Writes out date informaiton and tag information to
    the passed in arrays using passed in info
    """
    
    # find date info
    title_el = info.find('.//dates')
    date = title_el.attrib['taken']
    dateslist.append(date)
    
    # append tag info
    tags = []
    tag_el = info.find('.//tags')
    
    for tag in tag_el.findall('.//tag'):
        tags.append(tag.text)
        
    tagslist.append(tags)
    
    
    

api_key = 'c00650da0ba4205d2d759eea1b51f108'
flickr = flickrapi.FlickrAPI(api_key, cache=True)

# only retrieves images with geotagging data
photos = flickr.photos_search(tags='golden gate bridge', has_geo='1')
urllist = [] # store a list of what was downloaded
titlelist = [] # store a list of titles
latlist = [] # store a list of latitudes
lonlist = [] # store a list of longitudes
dateslist = [] # store a list of dates
tagslist = [] # store list of lists of tags for each image

#  returns first 100 photo 
for photo in photos[0][:100]:
    #store the id
    photo_id = photo.attrib['id']
    
    #get needed exif information
    info = flickr.photos_getInfo(photo_id = photo.attrib['id'])
    write_info(info, dateslist, tagslist)
    
    #get the required information
    titlelist.append(photo.attrib['title'])
    photoLoc = flickr.photos_geo_getLocation(photo_id = photo.attrib['id'])
    latlist.append(photoLoc[0][0].attrib['latitude'])
    lonlist.append(photoLoc[0][0].attrib['longitude'])
    photoSizes = flickr.photos_getSizes(photo_id = photo.attrib['id'])
    
    # size [0][3] corresponds to a medium sized image
    url = photoSizes[0][3].attrib['source']
    urllist.append(url) 
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urlparse.urlparse(url).path)) 
    print 'downloading:', url

fl = open('urls.txt', 'w')
for url in urllist:
    fl.write(url+'\n')
fl.close()

fl2 = open('titles.txt', 'w')
for name in titlelist:
	try:
		fl2.write(name+'\n')
	except:
		fl2.write('\n')
fl2.close()

fl3 = open('lat.txt', 'w')
for lat in latlist:
    fl3.write(lat+'\n')
fl3.close()

fl4 = open('lon.txt', 'w')
for lon in lonlist:
    fl4.write(lon+'\n')
fl4.close()

#write out dates
fl5 = open('dates.txt', 'w')
for date in dateslist:
    fl5.write(date + '\n')
fl5.close()

#write out tags
fl6 = open('tags.txt', 'w')
for tags in tagslist:
    for tag in tags:
        fl6.write(tag + ' ')
    fl6.write('\n')
fl6.close()
