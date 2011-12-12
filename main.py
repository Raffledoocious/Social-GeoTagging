import os
import glob
# using the simplekml modules http://code.google.com/p/simplekml/
import simplekml
from parsephotos import parse_clusters


# make a list out of the lines of a text file
def makeList(filename):
	f = open(filename, 'r')
	list = f.readlines()
	f.close()
	return list


# according to this we can't color the white icon, need to be separate icons
# http://groups.google.com/group/kml-support-getting-started/browse_thread/thread/e41698f1fa94cfe0
def returnColor(color):
	if color=='red':
		return 'http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png'
	elif color=='blue':
		return 'http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png'
	elif color=='green':
		return 'http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png'
	elif color=='yellow':
		return 'http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'
	elif color=='purple':
		return 'http://maps.google.com/mapfiles/kml/pushpin/purple-pushpin.png'
	else:
		return 'http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png'
		

# makes a kml file given a set of photos and a destination file name
def makeKML(thePhotos, filename):
	kml = simplekml.Kml()
	for photo in thePhotos:
		pnt = kml.newpoint(name=photo['title'], coords=[(photo['lon'],photo['lat'])])
		pnt.iconstyle.icon.href = photo['iconcolor']
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
	photos.append({'title':titlesList[i].rstrip('\r\n'), 'lat':latsList[i].rstrip('\r\n'), 'lon':lonsList[i].rstrip('\r\n'), 'coordsum': float(latsList[i]) + float(lonsList[i]), 'flickr':flickrurlsList[i].rstrip('\r\n'), 'file':files[i].rstrip('\r\n'), 'iconcolor':returnColor('')})
	
#parse out the photo clusters here, depending on arguments
clusters = parse_clusters(None, photos)


#testing here parsing out images
#kml_test = simplekml.Kml()
#for cluster in clusters.keys():
#	pin_photo = clusters[cluster][0]
#	kml_test.newpoint(name=pin_photo['title'], coords=[(pin_photo['lon'],pin_photo['lat'])])
#kml_test.save("test2.kml")

# returns a kml that clusters photos based on proximity
# photos taken in relatively the same area are colored the same
locationClusters = photos # locationClusters = parse_clusters(None, photos)
makeKML(locationClusters, 'location-cluster.kml')

# returns a kml that clusters photos based on color
# photos that are overall the same color are colored the same
colorClusters = photos # colorClusters = parse_clusters(None, photos)
makeKML(colorClusters, 'color-cluster.kml')

# returns a kml that clusters photos based on tags
# photos with similar colors are colored the same
tagClusters = photos # tagClusters = parse_clusters(None, photos)
makeKML(tagClusters, 'tag-cluster.kml')
