from flask import Flask, request, redirect
from src.auth.auth import get_authorization_url, get_access_token
from src.data.api_request import get_user_top_items

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect user to Spotify login
    auth_url = get_authorization_url()
    return redirect(auth_url)

@app.route('/callback/')
def callback():
    # Get authorization code from Spotify
    auth_code = request.args.get('code')
    
    # Exchange authorization code for access token
    access_token = get_access_token(auth_code)
    
    # Fetch user's top tracks
    top_tracks = get_user_top_items(access_token, item_type='tracks', time_range='long_term')
    
    # Display the results
    return top_tracks  # You'll likely want to process or display this differently

if __name__ == '__main__':
    app.run(debug=True, port=8888)