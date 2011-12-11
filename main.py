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

titlesList = makeList('images/titles.txt')
latsList = makeList('images/lat.txt')
lonsList = makeList('images/lon.txt')
flickrurlsList = makeList('images/urls.txt')
files = glob.glob('images/*.jpg')

# holds all the info for the photos
photos = []

# populates a 2D array with the photo info
# photos[0]['title'] is the first photo's title, etc.
for i in range(len(titlesList)):
	photos.append({'title':titlesList[i], 'lat':latsList[i], 'lon':lonsList[i], 'coordsum': float(latsList[i]) + float(lonsList[i]), 'flickr':flickrurlsList[i], 'file':files[i]})
	
#parse out the photo clusters here, depending on arguments
clusters = parse_clusters(None, photos)

#testing here parsing out images
kml_test = simplekml.Kml()
for cluster in clusters.keys():
	pin_photo = clusters[cluster][0]
	kml_test.newpoint(name=pin_photo['title'], coords=[(pin_photo['lon'],pin_photo['lat'])])

kml_test.save("test2.kml")

# kml file
kml = simplekml.Kml()

for photo in photos:
	kml.newpoint(name=photo['title'], coords=[(photo['lon'],photo['lat'])])
kml.save("test.kml")