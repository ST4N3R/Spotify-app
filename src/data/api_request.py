import requests


def get_user_top_items(access_token, item_type='tracks', time_range='medium_term', limit=20):
    """Gets the data from GET USE'S TOP ITEMS API

    Args:
        access_token (str): code that gives access to the API
        item_type (str, optional): specifies what type of data we get - tracks or artists. Defaults to 'tracks'.
        time_range (str, optional): specifies from what period we get the data. Defaults to 'medium_term'.
        limit (int, optional): set the limit of reposnds, max 50. Defaults to 20.

    Returns:
        _type_: _description_
    """

    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    url = f"https://api.spotify.com/v1/me/top/{item_type}"
    params = {
        'time_range': time_range,
        'limit': limit 
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json() 