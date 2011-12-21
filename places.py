# example URL
# https://maps.googleapis.com/maps/api/place/search/xml?location=37.82645,-122.42323&radius=50&sensor=false&key=AIzaSyCtc-W3m2xFf_j9Qi4Axvfqe2lonkR2Uy8&type=point_of_interest

import simplejson
import urllib

API_KEY = 'AIzaSyCtc-W3m2xFf_j9Qi4Axvfqe2lonkR2Uy8'
GOOGLEMAPS = 'https://maps.googleapis.com/maps/api/place/search/json'
RADIUS = 500

def search(coords, radius):
	url = GOOGLEMAPS + '?location=' + coords + '&radius=' + str(radius) + '&sensor=false&key=' + API_KEY + '&type=point_of_interest'
	#print(url)
	# json data returned from Google Places API request
	result = simplejson.load(urllib.urlopen(url))
	return result

def newLandmarks(lat,lon):
	coords = makeCoords(lat,lon)
	places = search(coords, RADIUS)
	
	# landmarks is a list of all the places the request returned
	landmarks = []
	for place in places['results']:
		#print(place['name'])
		landmarks.append({'name':place['name'],'lat':place['geometry']['location']['lat'],'lon':place['geometry']['location']['lng'],'types':place['types']})
	
	# some of the landmarks aren't desirable so we can filter some out based on keywords
	filteredLandmarks = []
	for landmark in landmarks:
		foundGood = False
		foundBad = False
		for types in landmark['types']:
			if(types == 'establishment' or types == 'park' or types == 'neighborhood' or types == 'art_gallery' or types == 'aquarium' or types == 'museum' or types == 'stadium' or types == 'university' or types == 'zoo' or types == 'amusement_park' or types == 'airport' or types == 'city_hall' or types == 'campground' or types == 'natural_feature'):
				foundGood = True
			if(types == 'route' or types == 'school' or types == 'hospital' or types == 'post_office' or types == 'parking' or types == 'bank' or types == 'doctor' or types == 'dentist' or types == 'pharmacy' or types == 'spa' or types == 'cafe' or types == 'storage' or types == 'pharmacy' or types == 'bus_station' or types == 'transit_station'):
				foundBad = True
		if(foundGood == True and foundBad == False):
			filteredLandmarks.append(landmark)
	
	return filteredLandmarks
	
def makeCoords(lat, lon):
	return str(lat) + ',' + str(lon)
	