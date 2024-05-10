import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Retrieve secrets
def read_secrets(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        client_id = lines[0].strip().split(':')[1]
        client_secret = lines[1].strip().split(':')[1]
    return client_id, client_secret

# setup spotipy client
def retrieve_sp():
    # Read client ID and client secret from secrets.txt
    client_id, client_secret = read_secrets('secrets.txt')
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    return sp
