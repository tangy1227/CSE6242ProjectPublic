import sqlite3
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# This function takes a month as a string in the format 'YYYY-MM' and returns a list of the top 10 most similar regions and the bottom 10 least similar regions
conn = sqlite3.connect('data.db')
# month = '2017-01'

# Load the data for the specified month
# df = pd.read_sql_query(f"SELECT * from data WHERE Date LIKE '{month}%' ", conn)
df = pd.read_sql_query(f"SELECT * from data", conn)

# Load the country codes mapping file
country_codes = pd.read_csv('country_codes.csv', index_col='Code')

# Convert region codes to country names using the mapping file
df['Country'] = df['Region'].str.upper().map(country_codes['Name'])

# Pivot the data to create a matrix of region by track name, with the values being the number of streams
pivot_table = pd.pivot_table(df, values='Streams', index=['Country'], columns=['Track Name'], aggfunc=np.sum, fill_value=0)

normalized_matrix = pivot_table.apply(lambda x: x/x.sum(), axis=1)
cosine_similarity_matrix = cosine_similarity(normalized_matrix)
similarity_df = pd.DataFrame(cosine_similarity_matrix, index=pivot_table.index, columns=pivot_table.index)

print("Similarity matrix:")
print(similarity_df)

# Find the top 10 most similar regions
most_similar = similarity_df.unstack().sort_values(ascending=False).drop_duplicates()
most_similar = most_similar[most_similar.index.get_level_values(0) != most_similar.index.get_level_values(1)] # Exclude self-similarity
most_similar = most_similar.head(10)

# Find the bottom 10 least similar regions
least_similar = similarity_df.unstack().sort_values().drop_duplicates()
least_similar = least_similar[least_similar.index.get_level_values(0) != least_similar.index.get_level_values(1)]
least_similar = least_similar.head(10)

# Print the results
print("Top 10 most similar regions:")
for (region1, region2), similarity in most_similar.items():
    print(f"{region1}, {region2}, {similarity:.2f}")

print("\nBottom 10 least similar regions:")
for (region1, region2), similarity in least_similar.items():
    print(f"{region1}, {region2}, {similarity:.2f}")

# Save the results to CSV files
most_similar.to_csv('most_similar.csv', header=['Similarity'])
least_similar.to_csv('least_similar.csv', header=['Similarity'])

# Print a message indicating that the CSV files have been saved
print("CSV files saved: most_similar.csv, least_similar.csv")