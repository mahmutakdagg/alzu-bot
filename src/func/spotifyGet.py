import requests
from dotenv import load_dotenv
import os

load_dotenv()

def getToken():
    SpotifyClientID =os.getenv('SpotifyClientID')
    SpotifyClientSECRET =  os.getenv('SpotifyClientSECRET')

    head = { 'Content-Type': "application/x-www-form-urlencoded" }

    tokenGet = requests.post( "https://accounts.spotify.com/api/token", data = f"grant_type=client_credentials&client_id=a261ed3bb88942a0b08d130a40920462&client_secret=f4800157163347518ad94a2e017eb550", headers = head )
    
    jsonTOKEN = tokenGet.json()
    accessTOKEN = jsonTOKEN[ 'access_token' ]
    return accessTOKEN

AUTH = { "Authorization": f"Bearer { getToken() }" }

def getSpotifyUrl( hesap ):
    
    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }", headers = AUTH )
    APIjson = API.json()
    APIimages = APIjson[ "images" ][ 1 ]
    APIurl = APIimages[ 'url' ]


    return APIurl

def getDisplayName( hesap ):

    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }", headers = AUTH )
    APIjson = API.json()
    APIname = APIjson[ 'display_name' ]

    return APIname

def getFollowersCount( hesap ):

    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }", headers = AUTH )
    APIjson = API.json()
    APICount = APIjson[ 'followers' ][ 'total' ]
    
    return APICount


def getPlaylists(hesap):
    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }/playlists", headers = AUTH )
    APIjson = API.json()
    return APIjson[ 'items' ]


def searchAlbum(album):
    API = requests.get( f"https://api.spotify.com/v1/search?q={album}&type=album", headers = AUTH )
    APIjson = API.json()
    APIalbum = APIjson['albums']['items'][0]
    returnedValue = APIalbum['external_urls']['spotify']
    return returnedValue
