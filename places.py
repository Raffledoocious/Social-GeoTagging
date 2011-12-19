# 37.82645, -122.42323

# https://code.google.com/apis/console/#project:592678228075:access

# https://maps.googleapis.com/maps/api/place/search/xml?location=37.82645,-122.42323&radius=50&sensor=false&key=AIzaSyCtc-W3m2xFf_j9Qi4Axvfqe2lonkR2Uy8&type=point_of_interest

#http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CCIQFjAA&url=http%3A%2F%2Fwww.google.com%2Fgoogleblogs%2Fpdfs%2Fgoogle_landmark_recognition.pdf&ei=ebLvTvK9E-rl0QHk5vXQCQ&usg=AFQjCNGgpscI6HcZg_Mkm24DXvICHkPmAg&sig2=y6aPkZN6QqjEUauizzohXg

import simplejson
import urllib

API_KEY = 'AIzaSyCtc-W3m2xFf_j9Qi4Axvfqe2lonkR2Uy8'
GOOGLEMAPS = 'https://maps.googleapis.com/maps/api/place/search/json'
COORDS = '37.82645,-122.42323'
RADIUS = 50

def search(coords, radius):
	url = GOOGLEMAPS + '?location=' + coords + '&radius=' + str(radius) + '&sensor=false&key=' + API_KEY + '&type=point_of_interest'
	result = simplejson.load(urllib.urlopen(url))
	return result
	

places = search(COORDS, 50)
for place in places['results']:
	print(place['name'])
	