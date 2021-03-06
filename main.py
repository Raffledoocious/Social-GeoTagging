import os
import glob
# using the simplekml modules http://code.google.com/p/simplekml/
import simplekml
import sys
from parsephotos import parse_clusters
from cluster.utility import returnColor
from places import newLandmarks

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
		#print(photo['flickr'])
		pnt = kml.newpoint()
		# try this in case we get a non-ascii character that can't be encoded
		try:
			name = unicode(photo['title'])
		except:
			name = 'untitled'
		pnt.name=name
		# add the Flickr link to the photo's description
		pnt.description=photo['flickr']
		pnt.coords=[(photo['lon'],photo['lat'])]
		pnt.iconstyle.color = photo['iconcolor']
		pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png'
	kml.save(filename)


titlesList = makeList('images/titles.txt')
latsList = makeList('images/lat.txt')
lonsList = makeList('images/lon.txt')
flickrurlsList = makeList('images/urls.txt')
dateslist = makeList('images/dates.txt')
tagslist = makeList('images/tags.txt')
files = glob.glob('images/*.jpg')

# holds all the info for the photos
photos = []

# populates a 2D array with the photo info
# photos[0]['title'] is the first photo's title, etc.
# .rstrip removes the newline characters from strings
for i in range(len(titlesList)):
	photos.append({'title':titlesList[i].rstrip('\r\n'), 'lat':float(latsList[i].rstrip('\r\n')), 'lon':float(lonsList[i].rstrip('\r\n')), 'flickr':flickrurlsList[i].rstrip('\r\n'), 'file':files[i].rstrip('\r\n'), 'date':dateslist[i].rstrip('\r\n'), 'tags':tagslist[i].rstrip('\r\n'), 'iconcolor':'ffffffff'})

# returns a kml that clusters photos based on proximity
# photos taken in relatively the same area are colored the same
locationData = parse_clusters("geotag", photos)
locationClusters = locationData['photos']
makeKML(locationClusters, 'location-cluster.kml')


# returns a kml that identifies new landmarks based on previous clusters
# also returns a text file of a list of the landmarks
locationClusterData = locationData['clusters']
landmarks = []
for entry in locationClusterData:
	#print(str(entry['lat']) + ', ' + str(entry['lon']))
	landmarks.append(newLandmarks(str(entry['lat']),str(entry['lon'])))

kml = simplekml.Kml()
landmarksText = open('landmarks.txt', 'w')
for landmark in landmarks:
	for place in landmark:
		pnt = kml.newpoint(name=place['name'], coords=[(place['lon'],place['lat'])])
		pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png'
		try:
			name = unicode(place['name'])
			landmarksText.write(name + '\n')
		except:
			pass
	kml.save('landmarks.kml')
landmarksText.close()

# returns a kml that clusters photos based on date
# photos taken are categorized into three predefined buckets
dateClusters = parse_clusters('date', photos)
makeKML(dateClusters, 'date-clusters.kml')


# returns a kml that clusters photos based on color
# photos that are overall the same color are colored the same
colorClusters = parse_clusters("color", photos)
makeKML(colorClusters, 'color-cluster.kml')


# returns a kml that clusters photos based on a tag
# photos with a common tag are clustered by same color pin
tagClusters = parse_clusters('tag', photos)
makeKML(tagClusters, 'tag-cluster.kml')
