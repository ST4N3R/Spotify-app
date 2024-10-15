import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET_ID = os.getenv('CLIENT_SECRET_ID')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPES = "user-top-read"