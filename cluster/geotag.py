"""

Geotag clustering - clusters an array of images on geotag information

"""
from collections import defaultdict
from utility import gen_hex_color
import random
import math

#current default radius for clustering
DISTANCE = 2
CLUSTER_COUNT = 7
ERROR_VAL = 1
MAX_ITERATIONS = 500

def get_centroids(photos):
    """
    Gets the centroids used in K-means computation
    """
    
    max_int = len(photos) - 1
    used_colors = {}
    centroids = []
    
    #get the random images
    selections = random.sample(range(0, max_int), CLUSTER_COUNT)

    #assign random unique colors
    for selection in selections:
        new_color = gen_hex_color(used_colors)
        photo = photos[selection]
        photo['iconcolor'] = new_color
            
        centroids.append({'lat':float(photo['lat']), 'lon':photo['lon'], 'color':new_color, 'photos':[]})
    
    return centroids

def assign_photo(photo, clusters):
    """
    Assigns a photo to a previously computed cluster
    
    """
    min_dist = float('inf')
    assigned_cluster = 0
    
    for selection in range(0, len(clusters)):
        distance = math.sqrt( (clusters[selection]['lat'] - photo['lat'])**2 + (clusters[selection]['lon'] - photo['lon'])**2 )
        
        #do comparison on the distance
        if (distance < min_dist):
            min_dist = distance
            assigned_cluster = selection
    
    clusters[assigned_cluster]['photos'].append(photo)
        
def compute_new_averages(centroids):
    """
    Computes the new points to use a centers in the clustering alg
    """
    for cluster in centroids:
        photos = cluster['photos']
        if (len(photos) > 0):
            long_sum = 0
            lat_sum = 0
            
            #iterate through photos to compute average
            for photo in photos:
                long_sum += photo['lon']
                lat_sum += photo['lat']
            cluster['lat'] = lat_sum / len(cluster['photos'])
            cluster['lon'] = long_sum / len(cluster['photos'])
            
def clear_clusters(clusters):
    """
    Removes all photos from all clusters for next iteration
    """
    
    for cluster in clusters:
        cluster['photos'] = []
        
def assign_final_colors(photos, clusters):
    """
    Assign final pin color based on the final clustering
    """
    
    for cluster in clusters:
        cluster_photos = cluster['photos']
        
        #iterate through each photo in each cluster
        for cluster_photo in cluster_photos:
            
            #and each photo
            for photo in photos:
                
                #if file names match...assign the cluster color to the photo
                if (cluster_photo['file'] == photo['file']):
                    photo['iconcolor'] = cluster['color']
                    break
                
def k_means(photos, centroids):
    """
    k-means clustering implementation using default cluster
    and default iteration count
    """
    iterations = 0
    changed = False
    
    #iterate until all clusters are settled or max iterations reached
    while iterations < MAX_ITERATIONS and not changed:
        
        #clear all clusters
        clear_clusters(centroids)
        
        #assign each photo
        for photo in photos:
            assign_photo(photo, centroids)
        
        compute_new_averages(centroids)
        
        iterations += 1
        
    #now assign colors based on final cluster to the photos
    assign_final_colors(photos, centroids)
    
    return photos

def cluster_photos(photos):
    """
    Clusters photos based on summation of their values
    
    photos: the photo dictionary
    
    """
     
    clusters = {}
    used_colors = {}
    count = 0
    
    centroids = get_centroids(photos)
    k_means(photos, centroids)
    
    return photos

def parse_geotag_clusters(photos):
    """
    
    Parses out the geotag clusters from a passed in image array
    
    photos: The photo dictionary
    
    """ 
    clusters = cluster_photos(photos)
    return clusters

# for testing purposes
if __name__ == "__main__":
    pass
