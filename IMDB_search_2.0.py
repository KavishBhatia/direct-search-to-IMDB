import sys
import urllib.request as ur
import json
import webbrowser
from easygui import *

# name = "manikarnika"
key = "" #enter your api key here from omdb.com
api = "&apikey="
omdb = "http://www.omdbapi.com/?t="
imdb = "https://www.imdb.com/title/"


def getName(name):
    name = name.split()
    if len(name) > 1:
        new_name = ""
        for i in name:
            new_name += i + "+"
        new_name = new_name[:-1]    
        return(new_name)
    else:
        name = name[0]
        return(name)


def getUrl(name):
    url = omdb + getName(name) + api + key
    print(url)
    return(url)


def getResponse(url):
    response = ur.urlopen(url).read()
    jsonvalues = json.loads(response)
    response = jsonvalues["Response"]
    imdbID = jsonvalues['imdbID']
    return response,imdbID

def openUrl(imdbid):
    movieurl = imdb + imdbid
    print(movieurl)
    webbrowser.open(movieurl)

def guibox():
    name = enterbox("Enter Movie Name")
    return(name)


def main():
    name = guibox()
    url = getUrl(name)
    resp,id = getResponse(url)
    
    if resp == "True":
        openUrl(id)


if __name__ == "__main__":
	# calling the main function
	main()
