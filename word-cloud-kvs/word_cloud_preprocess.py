import pandas as pd
from collections import Counter

# Step 1: Load the excel file
df = pd.read_excel("top_5_unique_updated_cleaned.xlsx")

# Step 2: Tokenize the lyrics
words = df["Clean Lyrics"].str.split(expand=True).stack()

# Step 3: Count the frequency of each word
word_counts = Counter(words)

# Step 4: Select the 20 most common words
top_words = [word for word, count in word_counts.most_common(200)]

print(top_words)

# # Step 5: Count the number of occurrences of each of the top 20 words in each song
# counts = []
# for i in range(len(df)):
#     lyrics = df.iloc[i]["Clean Lyrics"]
#     song_counts = [lyrics.count(word) for word in top_words]
#     counts.append(song_counts)

# # Step 6: Create a column for each word and fill it with the word count for that song
# for i, word in enumerate(top_words):
#     df[word] = [count[i] for count in counts]

# # Step 7: Update the excel file with the results
# df.to_excel("top_5_unique_updated_cleaned_preprocessed.xlsx", index=False)
