####################################
#           Libraries
####################################
import pandas as pd
import requests

####################################
#           Helper Functions
####################################
def search_track_id(song_name, artist_name, api_key):
    url = f'https://api.musixmatch.com/ws/1.1/matcher.track.get?q_track={song_name}&q_artist={artist_name}&apikey={api_key}'
    response = requests.get(url)
    json_data = response.json()
    try:
        # Check if any results were returned
        if json_data['message']['header']['status_code'] == 200:
            track_id = json_data['message']['body']['track']['track_id']
            return track_id
        else:
            return None
    except:
        print('*********************************')
        print('             Error               ')
        print('*********************************')
        print(url)
        print(json_data)
        return None

def get_lyrics(track_id, api_key):
    url = f'https://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={track_id}&apikey={api_key}'
    response = requests.get(url)
    json_data = response.json()
    try:
        # Check if any results were returned and if track_id is valid (sometimes it is not)
        if (json_data['message']['header']['status_code'] == 200) and (track_id is not None):
            lyrics = json_data['message']['body']['lyrics']['lyrics_body']
            # Remove the last line of the lyrics which contains a disclaimer
            lyrics = lyrics[:-70]
            return lyrics
        else:
            return None
    except:
        print('*********************************')
        print('             Error               ')
        print('*********************************')
        print(url)
        print(json_data)
        return None

####################################
#            Main
####################################
# Song Data
input_file = "top_5_unique.xlsx"

# Results File
output_file = input_file[:-5] + "_updated.xlsx"

# MusixMatchAPI key
api_key = "4de847499f2b28268a36d4b7a9023aa6" # First: ksastry3@gatech.edu
# api_key = "b8846eae7c32215b435dbf2af812465e" # Second: kvs@gatech.edu

# Load the excel file into a pandas dataframe
print('Loading input data from' + input_file + '...')
df = pd.read_excel(input_file)
print('Done.')

# Use Song Name and Artist to get Track ID, add Track ID column to dataframe
print('Getting Track IDs...')
df['Track ID'] = df.apply(lambda row: search_track_id(row['Track Name'], row['Artist'], api_key), axis=1)
print('Done.')

# Use Track ID to get Lyrics, add Lyrics column to dataframe
print('Getting Lyrics...')
df['Lyrics'] = df['Track ID'].apply(lambda track_id: get_lyrics(track_id, api_key))
print('Done.')

# Save the dataframe to an Excel file
print('Saving results to' + output_file + '...')
df.to_excel(output_file, index=False)
print('Done.')
