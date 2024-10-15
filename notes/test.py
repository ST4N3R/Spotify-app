import os
import requests
import json
import urllib.parse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")  # Your registered redirect URI
DECODED_SCOPE = "user-top-read"
SCOPE = urllib.parse.quote(DECODED_SCOPE)

'''
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

W przykładzie ze strony spotify widnieje takie zapytanie. Wszystkie jego elementy są widoczne w poniższej funkcji.
-X to url
-H to headers
-d to data
'''

# Get access token
# def get_access_token():
#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
#     data = {
#         "grant_type": "client_credentials",
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#     }
    
#     response = requests.post(url, headers=headers, data=data)
#     response_data = response.json()
    
#     return response_data['access_token']


def get_access_token(auth_code):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    
    response = requests.post(url, headers=headers, data=data)
    print(response)
    return response.json()['access_token']


def get_authorization_url():
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
    }
    
    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    print(f"Visit this URL to authorize the app: {url}")


def get_artist_data(artist_id: str, token: str):
    #https://api.spotify.com/v1/artists/{id}

    url = "https://api.spotify.com/v1/artists/" + artist_id
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_artist_albums(artist_id: str, token: str):
    #https://api.spotify.com/v1/artists/{id}/albums
    #Argumenty podajemy po ?

    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album%2C+single"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_artist_top_tracks(artist_id: str, token: str):
    #https://api.spotify.com/v1/artists/{id}/top-tracks

    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_artist_related_artists(artist_id: str, token: str):
    #https://api.spotify.com/v1/artists/{id}/related-artists
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_album(album_id: str, token: str):
    #https://api.spotify.com/v1/artists/{id}/related-artists
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_saved_albums(token):
    url = "https://api.spotify.com/v1/me/albums"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def check_if_saved_album(album_id, token):
    url = f"https://api.spotify.com/v1/me/albums/contains?ids={album_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def search(q, type, token):
    url = f"https://api.spotify.com/v1/search?q={q}&type={type}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def get_saved_tracks(token):
    url = f"https://api.spotify.com/v1/me/tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def get_top_items(token):
    url = f"https://api.spotify.com/v1/me/top/artists"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()



# Call the function to get the token
# token = get_access_token()

artist_id = "0TnOYISbd1XYRBk9myaseg"    #Pitbull
album_id = "76N6imyjQ9h5p2NzakHT32"     #M.I.A.M.I

# artist_data = get_artist_data("0TnOYISbd1XYRBk9myaseg", token)
# print("Artist Data:", json.dumps(artist_data, indent=4))

# artist_album = get_artist_albums(artist_id, token)
# print("Aritist albums: ", json.dumps(artist_album, indent=4))

# artist_top_tracks = get_artist_top_tracks(artist_id, token)
# print("Arist's top tracks", json.dumps(artist_top_tracks, indent=4))

# arist_related_artists = get_artist_related_artists(artist_id, token)
# print("Arist's related artists", json.dumps(arist_related_artists, indent=4))

# album_data = get_album(album_id, token)
# print("Album: ", json.dumps(album_data, indent=4))

# get_authorization_url()

auth_code = "AQCVi6coQVhY99X13-6V7oqyE-G1mKl1Yw_qpilE2BO_lwgBAT14gcr5dcrNnxlNl-BG8blSNeorwEmy8gUfiK1OITswq3CKYAUULWeyDjU-sF1-XT5QGzennpKTzj7fmc9Fsw3XkvgoJfl9pnOlvs_v7YBeXXfkSkwb3k0muxOGlrhmxnhBg74H5cOezFgtew"
# token = get_access_token(auth_code)
# print(token)
token = "BQAbWLI2-hNKCy326zVHK1RrsMrz-ly0kyWZQ10ChNSIYFf0-QJl60_PWivFhKVEPN1U8j1bkUBLgd2D0iZDiKLLZ-ZZcRxlwY8HMJxDZGp5nFj-PEmAiMRBS5ptUqU7DKzqSFnGO0QO3Cy94LDsSpXJon0dMKjO1AbJc5Vm7t0pyUeQfHaSrmY4_Vxyuixv_uc"

# saved_ablums = get_saved_albums(token)
# print("Saved albums: ", json.dumps(saved_ablums, indent=4))

# is_saved_album = check_if_saved_album(album_id, token)
# print(f"Album {album_id} is saved - {is_saved_album}")

# search_result = search(q="artist:Pitbull", type="album", token=token)
# print("Search results: ", json.dumps(search_result, indent=4))

# saved_tracks = get_saved_tracks(token)
# print("Saved tracks ", json.dumps(saved_tracks, indent=4))

top_items = get_top_items(token)
print("You recently played: ", json.dumps(top_items, indent=4))