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
import requests
import sys

#---------------------------------GET-------------------------------------------
url = 'http://localhost:7878/api/movies/command?apikey=f7478ccfcd3d4f2da5d5583228df15c9'
print("Querying... {} \n".format(url))

params = {"title":"Assasin's Creed"}

get_response = requests.get(url = url, params = params)
print("url_response: {} \n".format(get_response))

get_response_data = get_response.json()
print("response_data: \n {} \n".format(get_response_data))


def get_movie_by_id(url, id):
    params = {"id" : "{}".format(int(id))}
    get_response = requests.get(url = url, params = params)
#---------------------------------GET-------------------------------------------

#---------------------------------POST------------------------------------------
def post_movie(url, title, qualityProfileId, titleSlug, images, tmdbId, year, path, monitored = False):

    try:
        new_movie = {
        "title" : "{}".format(str(title)), #string
        "qualityProfileId" : "{}".format(int(qualityProfileId)), #int
        "titleSlug" : "{}".format(str(titleSlug)), #string
        "images" : "{}".format(images), #array
        "tmdbId" : "{}".format(int(tmdbId)), #int
        "year" : "{}".format(int(year)), #int
        "path" : "{}".format(str(path)), #string
        "monitored" : "{}".format(monitored) #boolean
        }

        #creates new json object
        new_movie = json.dumps(new_movie)
        print("json_object: \n {}".format(new_movie))

        post_response = requests.post(url = url, data = new_movie)
    except ValueError as err:
        print("An error occured: {} \n exiting...".format(err))
        exit

#---------------------------------POST------------------------------------------

def main():
    url = 'http://localhost:7878/api/movies/command?apikey=f7478ccfcd3d4f2da5d5583228df15c9'

    title = "Assassin's Creed"
    qualityProfileId = 6
    titleSlug = "assassins-creed-121856"
    image = [{
    "coverType": "poster",
    "url": "/radarr/MediaCover/1/poster.jpg?lastWrite=636200219330000000"},
    {
    "coverType": "banner","url": "/radarr/MediaCover/1/banner.jpg?lastWrite=636200219340000000"
    }]
    tmdbId = 121856
    year = 2016
    path = "/path/to/Assassin's Creed (2016)"

    post_movie(url, title, qualityProfileId, titleSlug, image, tmdbId, year, path)

if __name__ == '__main__':
    main()

















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
