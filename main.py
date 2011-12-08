import os
import glob
import simplekml

files = glob.glob('images/*.jpg')

kml = simplekml.Kml()
kml.newpoint(name="test2", coords=[(18.432314,-33.988862)])
kml.save("test.kml")
