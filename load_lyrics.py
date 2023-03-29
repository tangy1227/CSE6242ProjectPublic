import requests
import json

class Musixmatch:
    def __init__(self) -> None:
        self.url = "http://api.musixmatch.com/ws/1.1/"
        # only have access to 30% of the lyrics with this non-commercial api
        # allow only 2000 Api Calls per day and 500 Lyrics display per day
        self.apikey = "59fb06124dfae411942f1a5d57a8ba0c"
        
    def _request(self, url: str) -> dict:
        request = requests.get(url)
        return request.json()
    
    def getURL(self, parameter) -> str:
        return f"{self.url}{parameter}&apikey={self.apikey}"
    
    def trackSearch(self, q_track, q_artist, page_size=1, page=1, format="_json"):
        """
        Input track name and artist name
        Return track ID
        """
        data = self._request(
            self.getURL(
                "track.search?"
                "q_track={}"
                "&q_artist={}"
                "&page_size={}"
                "&page={}"
                "&format={}".format(
                    q_track, q_artist, page_size, page, format
                )
            )
        )
        track_id = data["message"]["body"]["track_list"][0]["track"]["track_id"]
        return track_id
    
    def getLyrics(self, q_track, q_artist):
        trackID = self.trackSearch(q_track, q_artist)
        lyricsData = self._request(
            self.getURL(
                "track.lyrics.get?"
                "track_id={}".format(trackID)
            )
        )
        lyrics = lyricsData["message"]["body"]["lyrics"]["lyrics_body"]
        words = lyrics.split()

        # Remove the end sentence "******* This Lyrics is NOT for Commercial use *******"
        index = words.index("...") 
        words = words[:index]
        # Remove '(', ')', ',' in the words
        clean_words = [s.replace('(', '').replace(')', '').replace(',','') for s in words]

        return clean_words


if __name__ == "__main__":
    musix = Musixmatch()

    # list of track names and their corresponding artist names
    track_list = ["Wild Blue", "Peaches (feat. Daniel Caesar, Giveon)"]
    artist_list = ["John Mayer", "Justin Bieber"]

    num_track = len(track_list)
    word_count = {}
    for i in range(num_track):
        lyrics = musix.getLyrics(track_list[i], artist_list[i])
        for word in lyrics:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    
    # return the combination of word appearence count for all tracks listed above
    sort = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
    print(sort)
    