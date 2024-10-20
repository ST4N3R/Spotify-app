from flask import Flask, request, redirect
from src.auth.auth import get_authorization_url, get_access_token
from src.processing.api_request import get_user_top_items
import json

app = Flask(__name__)

#Główna strona. Pierszą rzeczą, którą robi jest przekierowanie na stronę logowania Spotify i pobranie zgody na SCOPES. 
#Po otrzymaniu zgód API Spotify przekierowuje stronę na /callback
#TO DO: Dodać frontend
@app.route('/')
def home():
    auth_url = get_authorization_url()
    return redirect(auth_url)

#Najpierw pobiera odpowiednie tokeny, a nastepnie używa ich do pobrania danych z GET USER'S TOP ITEMS. Na końcu zwraca wyniki
#TO DO: Następnie powinien przesyłać dane do Azure i obrabiać je
@app.route('/callback/')
def callback():
    auth_code = request.args.get('code')    #Pobiera auth_code
    
    res_access_token = get_access_token(auth_code)
    access_token = res_access_token['access_token']
    refresh_token = res_access_token['refresh_token']
    
    top_tracks = get_user_top_items(access_token, item_type='tracks', time_range='long_term')

    items = top_tracks['items']
    next_url = top_tracks['next']

    with open("data/data_artists.json", "w") as json_file:
        json.dump(items, json_file, indent=4)

    return top_tracks

if __name__ == '__main__':
    app.run(debug=True, port=8888)