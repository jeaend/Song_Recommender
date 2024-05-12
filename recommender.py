import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import pickle
import numpy as np 
import random
from sklearn.cluster import KMeans

from spotipy_util import retrieve_sp

# Function to check if song is in the top 100, returns true if unser_input is in top_100
def is_hot_100(song, top_100):
    song = song.lower()
    # check if the song title or artist matches any entry 
    is_in_top_100 = (top_100['title'].str.lower() == song) | (top_100['artist'].str.lower() == song)
    return is_in_top_100.any()

# Function to get audio features using the Spotify API, return df
def get_audio_features(song):
    # Authenticate with Spotify API 
    sp = retrieve_sp()

    # Search for the song
    results = sp.search(q=song, limit=1)

    # Get track ID and audio features
    track_id = results['tracks']['items'][0]['id']
    audio_features_full = sp.audio_features(track_id)[0]

    # get the 10 features, return df
    audio_features = {key: audio_features_full[key] for key in list(audio_features_full.keys())[:11]}
    return pd.DataFrame.from_dict(audio_features, orient='index').transpose()

def scale_audio_features(features):
    # Load the scaler object from the pickle file
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return scaler.transform(features)

# Function to apply cluster model return cluster number
def determine_cluster(audio_features):
    # Scale data
    scaled_features = scale_audio_features(audio_features)

    # Load pre-trained cluster model
    with open('cluster_model.pkl', 'rb') as f:
        loaded_model, loaded_clusters = pickle.load(f)
    new_clusters = loaded_model.predict(scaled_features)[0]

    # Predict cluster for the given song's audio features
    return new_clusters

# Function to retrieve song from given cluster
def recommend_song_from_cluster(df, cluster):
    # return random song from df in given cluster
    cluster_df = df[df['cluster'] == cluster]
    return cluster_df.sample(1)

def song_recommender(top_100, spotify):
    user_input = input("Enter the song title or artist: ")
    if is_hot_100(user_input, top_100):
        other_song = top_100[top_100['artist'].str.lower() != user_input].sample(n=1).iloc[0]
        print(f"You might like: '{other_song['artist']}' - '{other_song['title']}'")
    else:
        # get audio feature of the input song 
        audio_features = get_audio_features(user_input)
        # Apply cluster model and recommend a song from the same cluster
        cluster = determine_cluster(audio_features)
        recommended_song = recommend_song_from_cluster(spotify, cluster)
        print(f"You might like: '{recommended_song['song_artist'].iloc[0]}' - '{recommended_song['song_title'].iloc[0]}'")