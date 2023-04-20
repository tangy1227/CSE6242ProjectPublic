####################################
#           Libraries
####################################
import re
import pandas as pd

####################################
#           Helper Functions
####################################
# Define a function to clean the lyrics
def clean_lyrics(lyrics):
    # Remove new lines, line breaks, carriage returns, punctuation, and convert to lowercase
    lyrics = lyrics.replace('\n', ' ').replace('\r', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').lower()

    # Remove profanity
    profanity_list = ["fuck", "fucking", "nigga", "bitch"]
    lyrics = re.sub("|".join(profanity_list), "", lyrics)

    # Remove uninsightful words
    uninsighful = ['a','an','the','and','or','of','to','in','on','at','by','with','for','from','that','this','these','those','some','any','all','every','many','much','more','most','some','few','little','several','i', 'me', 'you', 'que', 'la', 'no', 'de', 'my', 'yeah', 'it', 'te', 'en', 'je', "i'm", 'ik', 'y', 'le', 'yo', 'oh', 'un', 'we', 'se', 'is', 'like', 'du', 'na', 'your', "don't", 'up', 'die', 'ich', 'tu', 'so', 'ja', 'lo', 'el', 'be', 'just', 'got', 'love', 'e', 'but', 'tú', 'si', 'es', 'mi', 'do', 'go', 'when', 'er', 'con', 'pas', 'o', 'non', "it's", 'was', 'und', 'now', 'det', 'les', 'ya', 'out', 'ah', 'what', 'og', 'jeg', 'one', 'get', 'ma', 'hey', 'il', 'say', 'not', 'che', 'if', 'they', 'dans', 'ég', 'she', 'ti', 'mig', 'da', "you're", 'por', 'à', 'ben', "can't", 'can', 'never', 'wanna', 'eu', 'et', 'let', 'ooh', 'una', 'pero', 'ey', 'het', 'time', 'der', 'não', 'på', 'been', 'een', 'como', 'op', 'di', "pa'", 'her', 'vi', "'cause", 'jag', 'niet', 'nie', "ain't", "j'ai", 'har', 'man', 'è', 'are', 'al', 'að', 'back', 'uh', 'see', 'tell', 'take', 'des', 'eh', "m'n", 'quiero', "c'est", 'mí', 'met', 'den', 'shit', 'need', 'sé', 'sa', 'make', 'var', 'how', 'feel', 'mais', 'som', 'way', 'wie', 'sie', "j'suis", 'wir', 'auf', 'am', 'til', 'look', 'ist', 'jak', 'vai', 'maar', 'comme', 'dat', 'cuando', 'ella', 'nicht', 'em', 'nu', 'girl', 'va', 'too', "i've", 'ho', 'é', 'para', 'ne', 'right', 'já', 'he', 'ouais', 'ze', 'ayy', 'pour', 'could', 'mich', 'gang', 'mir', 'im', 'är', 'solo', 'per', 'ta', "that's", 'then', 'als','bin', 'las', 'plus', 'más', 'så', "i'll", 'heb', 'keep', 'kan', 'men', 'med', 'qui', 'los', 'bien', 'w', 'mal', 'bent', 'here', 'ay', 'porque', 'z', 'said', 'mij', 'qué', 'where', 'gonna', 'voor', 'life', 'um', 'even', 'ein', 'com', 'have', 'est', 'soy', 'van', 'why', 'jij', 's', 'mit', 'ça', 'bad', 'had', 'alles', 'tout', 'as', 'sur', 'mon', 'will', 'sin', 'away', 'alle', 'ekki', 'zu', 'das', 'mas', "we're", "won't", 'gotta', 'good', 'bra', 'off', 'amor', 'ci', 'mind', 'think', 'su', 'au', 'mama', 'tengo', 'elle', 'hoe', 'você', 'real', 'om', 'day', 'nothing', 'doch', 'vez', 'voy', 'todo', 'quiere', 'así', 'sono', "there's", 'nos', 'about', 'dan', 'está', 'son', 'us', 'noche', 'quando', 'boy', 'there', 'weet', 'och', 'von', 'oh-oh', 'over', 'ela', 'bu', 'put', 'une', 'eso', 'pra', 'who', 'myself', 'tak', 'á', 'nunca', 'vil', 'than', 'leave', 'really', 'tá', 'ver', "ikk'", 'hit', 'siempre', 'min', 'hier', 'í', 'meg', 'yeh', 'still', "let's", 'mami', 'ser', 'eres', 'sind', "'em", 'dit', 'made', 'pull', 'sei', 'young', 'sem', 'fait', 'ever', 'high', 'ehi', 'ce', 'hay', 'vida', 'hold', 'home', 'new', 'call', 'ni', 'ahora', 'ai', 'through', 'für', 'dig', 'af', 'vie', 'só', 'show', "gon'", 'conmigo', 'tiene', 'stay', 'kom', 'ha', 'were', 'things', 'moi', 'dem', 'för', 'wenn', 'only', 'wish', 'club', "bi'", 'feeling', 'knew', 'hoy', 'ka', 'nadie', 'around', 'noch', 'wat', 'esta', 'meu', 'god', 'anh', 'gusta']
    lyrics = " ".join([word for word in lyrics.split() if word not in uninsighful])

    # Return
    return lyrics

####################################
#            Main
####################################
# Song Data
input_file = "top_5_unique_updated.xlsx"

# Results File
output_file = input_file[:-5] + "_cleaned.xlsx"

# Load the Excel sheet into a pandas dataframe
df = pd.read_excel(input_file)

# Apply the clean_lyrics function to each row in the dataframe
df["Clean Lyrics"] = df["Lyrics"].apply(clean_lyrics)

# Save the updated dataframe to a new Excel file
df.to_excel(output_file, index=False)
