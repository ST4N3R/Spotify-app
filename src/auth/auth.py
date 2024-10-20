import requests
from urllib.parse import urlencode
from ..config.config import CLIENT_ID, CLIENT_SECRET_ID, REDIRECT_URI, SCOPES

def get_authorization_url() -> str:
    """Generates authentication url (that is required to generate authentication code) for given scopes

    Returns:
        str: url that enables users to log in to thiers spotify accoutn
    """

    auth_url = 'https://accounts.spotify.com/authorize'
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPES,
        'show_dialog': True
    }
    return f"{auth_url}?{urlencode(params)}"


def get_access_token(auth_code: str):
    """Generates access token for a given authentication code

    Args:
        auth_code (str): 

    Returns:
        str:  
    """

    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET_ID
    }
    response = requests.post(token_url, headers=headers, data=data)
    return response.json()


def get_new_access_token(refresh_token: str):
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID
    }
    response = requests.post(token_url, headers=headers, data=data)
    return response.json()