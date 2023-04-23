import requests
import json

class Musixmatch:
    def __init__(self, q_track_list, q_artist_list):
        self.url = "http://api.musixmatch.com/ws/1.1/"
        # only have access to 30% of the lyrics with this non-commercial api
        # allow only 2000 Api Calls per day and 500 Lyrics display per day
        self.apikey = "4de847499f2b28268a36d4b7a9023aa6"
        self.q_track_list = q_track_list
        self.q_artist_list = q_artist_list
        
    def _request(self, url: str):
        request = requests.get(url)
        return request.json()
    
    def getURL(self, parameter) -> str:
        return f"{self.url}{parameter}&apikey={self.apikey}"
    
    def cleanWords(self, word_list):
        stopwords_en = ["the", "and", "a", "an", "in", "of", "to", "that", "is", "was", "with", "for", "it", "on", "as", "be", "at", "by", "this", "which", "or", "not", "but", "from", "are", "have", "has", "had", "if", "when", "where", "who", "what", "how", "why", "then", "there", "their", "so", "such", "like", "just", "only", "out", "up", "down", "off", "over", "under", "again", "some", "most", "other", "every", "many", "few", "somebody", "anybody", "nobody", "all", "both", "each", "either", "neither", "none", "some", "much", "several", "enough", "plenty", "fewer", "more", "less", "too", "very", "a", "an", "the", "no", "any", "some", "much", "many", "few", "little", "lot", "most", "several", "enough", "plenty", "all", "both", "neither", "either", "every", "no one", "nobody", "nothing", "something", "anything", "everything", "everyone", "someone", "this", "that", "these", "those", "it", "its", "they", "them", "their", "our", "us", "we", "you", "your", "he", "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "themself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves"]
        stopwords_es = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las", "por", "un", "para", "con", "no", "una", "su", "al", "lo", "como", "más", "pero", "sus", "le", "ya", "o", "fue", "este", "ha", "sí", "porque", "esta", "entre", "cuando", "muy", "sin", "sobre", "también", "me", "hasta", "hay", "donde", "quien", "desde", "todo", "nos", "durante", "hell"]
        uninsighful = ['a','an','the','and','or','of','to','in','on','at','by','with','for','from','that','this','these','those','some','any','all','every','many','much','more','most','some','few','little','several','i', 'me', 'you', 'que', 'la', 'no', 'de', 'my', 'yeah', 'it', 'te', 'en', 'je', "i'm", 'ik', 'y', 'le', 'yo', 'oh', 'un', 'we', 'se', 'is', 'like', 'du', 'na', 'your', "don't", 'up', 'die', 'ich', 'tu', 'so', 'ja', 'lo', 'el', 'be', 'just', 'got', 'love', 'e', 'but', 'tú', 'si', 'es', 'mi', 'do', 'go', 'when', 'er', 'con', 'pas', 'o', 'non', "it's", 'was', 'und', 'now', 'det', 'les', 'ya', 'out', 'ah', 'what', 'og', 'jeg', 'one', 'get', 'ma', 'hey', 'il', 'say', 'not', 'che', 'if', 'they', 'dans', 'ég', 'she', 'ti', 'mig', 'da', "you're", 'por', 'à', 'ben', "can't", 'can', 'never', 'wanna', 'eu', 'et', 'let', 'ooh', 'una', 'pero', 'ey', 'het', 'time', 'der', 'não', 'på', 'been', 'een', 'como', 'op', 'di', "pa'", 'her', 'vi', "'cause", 'jag', 'niet', 'nie', "ain't", "j'ai", 'har', 'man', 'è', 'are', 'al', 'að', 'back', 'uh', 'see', 'tell', 'take', 'des', 'eh', "m'n", 'quiero', "c'est", 'mí', 'met', 'den', 'shit', 'need', 'sé', 'sa', 'make', 'var', 'how', 'feel', 'mais', 'som', 'way', 'wie', 'sie', "j'suis", 'wir', 'auf', 'am', 'til', 'look', 'ist', 'jak', 'vai', 'maar', 'comme', 'dat', 'cuando', 'ella', 'nicht', 'em', 'nu', 'girl', 'va', 'too', "i've", 'ho', 'é', 'para', 'ne', 'right', 'já', 'he', 'ouais', 'ze', 'ayy', 'pour', 'could', 'mich', 'gang', 'mir', 'im', 'är', 'solo', 'per', 'ta', "that's", 'then', 'als','bin', 'las', 'plus', 'más', 'så', "i'll", 'heb', 'keep', 'kan', 'men', 'med', 'qui', 'los', 'bien', 'w', 'mal', 'bent', 'here', 'ay', 'porque', 'z', 'said', 'mij', 'qué', 'where', 'gonna', 'voor', 'life', 'um', 'even', 'ein', 'com', 'have', 'est', 'soy', 'van', 'why', 'jij', 's', 'mit', 'ça', 'bad', 'had', 'alles', 'tout', 'as', 'sur', 'mon', 'will', 'sin', 'away', 'alle', 'ekki', 'zu', 'das', 'mas', "we're", "won't", 'gotta', 'good', 'bra', 'off', 'amor', 'ci', 'mind', 'think', 'su', 'au', 'mama', 'tengo', 'elle', 'hoe', 'você', 'real', 'om', 'day', 'nothing', 'doch', 'vez', 'voy', 'todo', 'quiere', 'así', 'sono', "there's", 'nos', 'about', 'dan', 'está', 'son', 'us', 'noche', 'quando', 'boy', 'there', 'weet', 'och', 'von', 'oh-oh', 'over', 'ela', 'bu', 'put', 'une', 'eso', 'pra', 'who', 'myself', 'tak', 'á', 'nunca', 'vil', 'than', 'leave', 'really', 'tá', 'ver', "ikk'", 'hit', 'siempre', 'min', 'hier', 'í', 'meg', 'yeh', 'still', "let's", 'mami', 'ser', 'eres', 'sind', "'em", 'dit', 'made', 'pull', 'sei', 'young', 'sem', 'fait', 'ever', 'high', 'ehi', 'ce', 'hay', 'vida', 'hold', 'home', 'new', 'call', 'ni', 'ahora', 'ai', 'through', 'für', 'dig', 'af', 'vie', 'só', 'show', "gon'", 'conmigo', 'tiene', 'stay', 'kom', 'ha', 'were', 'things', 'moi', 'dem', 'för', 'wenn', 'only', 'wish', 'club', "bi'", 'feeling', 'knew', 'hoy', 'ka', 'nadie', 'around', 'noch', 'wat', 'esta', 'meu', 'god', 'anh', 'gusta']
        profanity_list = ["fuck", "shit", "nigga", "bitch", "ass", "pussy", "hoe", "damn", "percocets", "molly", "thots", "thot"]
        punctuations = '.,!?;:()[]{}<>"\'-'
        stopwords = stopwords_en + stopwords_es + uninsighful
        filtered_words = []
        for word in word_list:
            bad = False
            word = word.lower()
            # Clean Bad words
            for badword in profanity_list: 
                if badword in word:
                    bad = True
                    break
            # Clean punctuations
            if word not in stopwords and bad == False: 
                new_word = ''.join([char for char in word if char not in punctuations])
                # Clean numbers
                if not any(char.isdigit() for char in new_word): 
                    filtered_words.append(new_word)
        return filtered_words
    
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
            clean_words = self.cleanWords(words)
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

    track_list = ["Wild Blue", "Peaches (feat. Daniel Caesar, Giveon)"]
    artist_list = ["John Mayer", "Justin Bieber"]

    # track_list = ['Reggaetón Lento (Bailemos)', 'Chantaje', 'Otra Vez (feat. J Balvin)', "Vente Pa' Ca", 'Safari']
    # artist_list = ['CNCO', 'Shakira', 'Zion & Lennox', 'Ricky Martin', 'J Balvin']
    # musix = Musixmatch(track_list, artist_list)
    # word_list, word_count = musix.word_appearance()
    # print(word_count)

    # word_list = ['30s', 'know', '100']
    # clean = musix.cleanWords(word_list)
    # print(clean)
    
