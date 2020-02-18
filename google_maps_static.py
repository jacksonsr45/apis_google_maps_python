import requests
import json


class Google_Maps_Static:
    def __init__(self, user_requires):
        """
        URL by google from google maps static
        """
        url = 'https://www.google.com/maps/api/staticmap?'
        """
        User API_KEY by google api 
        """
        api_key = user_requires['user_key']
        """
        Your location from maps 
        """
        location = user_requires['user_location']
        center = location
        """
        Value by zoom in map from you location
        """
        zoom = user_requires['location_zoon']
        """
        Request location, zoom, size, API_KEY from render map
        """
        r = requests.get(url +'center='+center+'&zoom='+str(zoom)+'&size=1024x768&key='+api_key)

        """
        Creating and open maps.png 
        """
        f = open( 'maps.png', 'wb')
        """
        Write Value by request in maps.png
        """
        f.write(r.content)
        f.close()

user_requires = {
    'user_key': 'your api_key',
    'user_location': 'your location',
    'location_zoon': 17,
}

Google_Maps_Static(user_requires)