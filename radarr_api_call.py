#-----------------------------------NOTES---------------------------------------
# json notes
## json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
## json.loads() — Takes a JSON string, and converts (loads) it to a Python object.


# All API endpoints are based off of /api
## if you access Radarr via http://localhost:7878
## the API root would be http://localhost:7878/api
# API key can be accessed and reset via Settings -> General


# API videos
## https://www.youtube.com/watch?v=Wvl7NdB9J9o&t=329s - api description
## https://www.youtube.com/watch?v=F1kZ39SvuGE&t=508s - BeautifulSoup tutorial

# https://github.com/Radarr/Radarr/wiki/API:Movie - the basics of playing with
## movies and radarr

# python tutorial on how to use basic api commands
## https://www.geeksforgeeks.org/get-post-requests-using-python/

# http response status
## https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

# Notes on general api commands:
## get (read) - returns movie based on id or 404 error
## post (create) - adds new movie to collection
## put/patch (update) - update existing movie
## delete (delete) - delete movie based on id


# Required parameters to add a movie to radarr:
## title (string)
## qualityProfileId (int)
## titleSlug (string)
## images (array)
## tmdbId (int)
## year (int) release year. Very important needed for the correct path!
## path (string) - full path to the movie on disk or rootFolderPath (string) -
### full path will be created by combining the rootFolderPath with the movie title

## Optional parameters:
### monitored (bool) - whether the movie should be monitored or not.
### addOptions (object) - should contain a searchForMovie (string) key
#### with a bool value
#-----------------------------------NOTES---------------------------------------

import json
from bs4 import BeautifulSoup
import requests


#---------------------------------GET-------------------------------------------
url = 'http://localhost:7878/api/movies/command?apikey=f7478ccfcd3d4f2da5d5583228df15c9'
print("Querying... {} \n".format(url))

params = {"title":"Assasin's Creed"}

get_response = requests.get(url = url, params = params)
print("url_response: {} \n".format(get_response))

get_response_data = get_response.json()
print("response_data: \n {} \n".format(get_response_data))
#---------------------------------GET-------------------------------------------

#---------------------------------POST------------------------------------------
url = 'http://localhost:7878/api/movies/command?apikey=f7478ccfcd3d4f2da5d5583228df15c9'
print("Querying... {} \n".format(url))

# this might need to be json.dumps(new_movie) to convert it to a json object
new_movie = {
"title" : "{}".format(title),
"qualityProfileId" : "{}".format(qualityProfileId),
"titleSlug" : "{}".format(titleSlug),
"images" : "{}".forat(images),
"tmdbId" : "{}".format(tmdbId),
"year" : "{}".format(year),
"path" : "{}".format(path),
"monitored" : "{}".format(monitored)
}

post_response = requests.post(url = url, data = params)
print("url_response: {} \n".format(post_response))

#---------------------------------POST------------------------------------------



# def add_movie(url, title, qualityProfileId, titleSlug, images, tmdbid, year, path, monitored = False):


















# soup = BeautifulSoup(read_response, 'html.parser')
# json_object = json.loads(read_response)

# json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
# json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

#-------------------------------------------------------------------------------
# radarr_url = 'http://localhost:7878/api/addmovies'
#
# data = requests.get(radarr_url)
# soup = BeautifulSoup(data.text, 'html.parser')
#
# #finds first occurence of <script> tag and outputs it as text
# clean_soup = soup.find('script').text.split('=')[1].replace(';','')
#
# print("clean soup: \n {}".format(clean_soup))
#
# #wrap clean_soup in double quotes for json_object
# clean_soup = '"{}"'.format(clean_soup)
# print("quotes added clean_soup: \n {} ".format(clean_soup))
