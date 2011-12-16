import os
import glob
# using the simplekml modules http://code.google.com/p/simplekml/
import simplekml
from parsephotos import parse_clusters
from cluster.utility import returnColor

# make a list out of the lines of a text file
def makeList(filename):
	f = open(filename, 'r')
	list = f.readlines()
	f.close()
	return list



		

# makes a kml file given a set of photos and a destination file name
def makeKML(thePhotos, filename):
	kml = simplekml.Kml()
	for photo in thePhotos:
		pnt = kml.newpoint(name=photo['title'], coords=[(photo['lon'],photo['lat'])])
		pnt.iconstyle.color = photo['iconcolor']
	kml.save(filename)


titlesList = makeList('images/titles.txt')
latsList = makeList('images/lat.txt')
lonsList = makeList('images/lon.txt')
flickrurlsList = makeList('images/urls.txt')
files = glob.glob('images/*.jpg')

# holds all the info for the photos
photos = []

# populates a 2D array with the photo info
# photos[0]['title'] is the first photo's title, etc.
# .rstrip removes the newline characters from strings
for i in range(len(titlesList)):
	photos.append({'title':titlesList[i].rstrip('\r\n'), 'lat':float(latsList[i].rstrip('\r\n')), 'lon':float(lonsList[i].rstrip('\r\n')), 'flickr':flickrurlsList[i].rstrip('\r\n'), 'file':files[i].rstrip('\r\n'), 'iconcolor':'ffffffff'})
	
# returns a kml that clusters photos based on proximity
# photos taken in relatively the same area are colored the same
locationClusters = parse_clusters("geotag", photos)
makeKML(locationClusters, 'location-cluster.kml')

# returns a kml that clusters photos based on color
# photos that are overall the same color are colored the same
colorClusters = parse_clusters("color", photos)
makeKML(colorClusters, 'color-cluster.kml')

# returns a kml that clusters photos based on tags
# photos with similar colors are colored the same
#tagClusters = parse_clusters('tag', photos)
#makeKML(tagClusters, 'tag-cluster.kml')
