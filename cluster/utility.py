'''
Utility functions for image parsing

@author: Jared

'''


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