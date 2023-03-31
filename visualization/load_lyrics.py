import requests
import json

class Musixmatch:
    def __init__(self, q_track_list, q_artist_list) -> None:
        self.url = "http://api.musixmatch.com/ws/1.1/"
        # only have access to 30% of the lyrics with this non-commercial api
        # allow only 2000 Api Calls per day and 500 Lyrics display per day
        self.apikey = "59fb06124dfae411942f1a5d57a8ba0c"
        self.q_track_list = q_track_list
        self.q_artist_list = q_artist_list
        
    def _request(self, url: str) -> dict:
        request = requests.get(url)
        return request.json()
    
    def getURL(self, parameter) -> str:
        return f"{self.url}{parameter}&apikey={self.apikey}"
    
    def getLyrics(self, q_track, q_artist):
        lyricsData = self._request(
            self.getURL(
                "matcher.lyrics.get?"
                "q_track={}"
                "&q_artist={}".format(q_track, q_artist)
            )
        )
        if lyricsData["message"]["header"]["status_code"] != 404:
            lyrics = lyricsData["message"]["body"]["lyrics"]["lyrics_body"]
            words = lyrics.split()

            # Remove the end sentence "******* This Lyrics is NOT for Commercial use *******"
            if "..." in words:
                index = words.index("...") 
                words = words[:index]
            # Remove '(', ')', ',' in the words
            clean_words = [s.replace('(', '').replace(')', '').replace(',','') for s in words]
        else:
            clean_words = ["No-Lyrics-Data"]

        return clean_words

    def word_appearance(self):
        """
        Input list of track names and list of artist names
        Return word list, and their corresponding appearance count
        """
        num_track = len(self.q_track_list)
        word_count = {}
        for i in range(num_track):
            # print(self.q_track_list[i])
            # print(self.q_artist_list[i])
            lyrics = self.getLyrics(self.q_track_list[i], self.q_artist_list[i])
            for word in lyrics:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
        
        # return the combination of word appearence count for all tracks listed above
        sort = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

        word_list = [word[0] for word in sort]
        count_list = [count[1] for count in sort]
        return word_list, word_count

if __name__ == "__main__":
    # list of track names and their corresponding artist names
    track_list = ['Reggaetón Lento (Bailemos)', 'Chantaje', 'Otra Vez (feat. J Balvin)', "Vente Pa' Ca", 'Safari'] #["Wild Blue", "Peaches (feat. Daniel Caesar, Giveon)"]
    artist_list = ['CNCO', 'Shakira', 'Zion & Lennox', 'Ricky Martin', 'J Balvin'] #["John Mayer", "Justin Bieber"]
    musix = Musixmatch(track_list, artist_list)
    word_list, word_count = musix.word_appearance()
    