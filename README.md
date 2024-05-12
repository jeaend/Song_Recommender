# Song_Recommender
Recommender implemented using unsupervised machine learning, web scraping, and APIs to deliver personalized song recommendations. Utilizing clustering analysis on song features and data extraction techniques via web scraping and APIs, it provides tailored suggestions based on user input.


## Usage

1. Make sure you have a Spotify Developer account and create an app to obtain your client ID and client secret.
2. Save Spotify client ID and client secret as secrets.txt as follows:
```
clientid:c4cfff19516e40fa97e9fcf14b4db807
clientsecret:2df69a0559ad41a08427ea14f3a81e5a
```

## Cluster Descriptions

| Cluster | Description                                                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0       | - Low danceability and energy. - Moderate acousticness and instrumentalness. - Relatively low speechiness and liveness. - Moderate tempo.                          |
| 1       | - Moderate energy and valence. - Low acousticness and instrumentalness. - High liveness. - Moderate tempo.                                                          |
| 2       | - Very low danceability, energy, and valence. - Very high instrumentalness. - High acousticness. - High liveness. - Very low tempo.                                 |
| 3       | - Low energy and valence. - Moderate speechiness and liveness. - Moderate tempo.                                                                                    |
| 4       | - High danceability, energy, and tempo. - Moderate instrumentalness. - Low acousticness and liveness. - High valence.                                             |
| 5       | - Moderate energy, valence, and tempo. - Low instrumentalness. - Very high speechiness. - Very low acousticness. - Moderate liveness.                               |
| 6       | - Very low danceability, energy, and valence. - Very high instrumentalness. - High acousticness. - High liveness. - Very low tempo.                                  |
| 7       | - High danceability and energy. - Very high speechiness. - Low acousticness and instrumentalness. - Very low liveness. - Moderate tempo.                            |
| 8       | - High danceability, energy, and tempo. - Moderate speechiness and acousticness. - Low instrumentalness and liveness. - High valence.                                 |
| 9       | - High danceability, energy, and valence. - Moderate speechiness. - Low instrumentalness, liveness, and tempo.                                                     |
