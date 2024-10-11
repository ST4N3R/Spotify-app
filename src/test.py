import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET_ID")

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
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    
    return response_data['access_token']


def get_artist_data(artist_id: str, token: str):
    #https://api.spotify.com/v1/artists/{id}

    url = "https://api.spotify.com/v1/artists/" + artist_id
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()

# Call the function to get the token
token = get_access_token()

artist_data = get_artist_data("0TnOYISbd1XYRBk9myaseg", token)
print("Artist Data:", json.dumps(artist_data, indent=4))