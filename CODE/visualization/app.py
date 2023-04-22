from flask import Flask, jsonify, make_response, request
import pandas as pd
from load_lyrics import Musixmatch
import csv
import sqlite3

app = Flask(__name__)
region_map = {'ar': 'Argentina', 'at':'Austria', 'au':'Australia', 'be':'Belgium', 'bo':'Bolivia', 'br':'Brazil', 'ca':'Canada', 'ch':'Switzerland', 'cl':'Chile', 'co':'Colombia', 'cr':'Costa Rica', 'cz':'Czechia', 'de':'Germany', 'dk':'Denmark', 'do':'Dominican Republic', 'ec':'Ecuador', 'ee':'Estonia', 'es':'Spain', 'fi':'Finland', 'fr':'France', 'gb':'UK', 'global':'Global', 'gr':'Greece', 'gt':'Guatemala', 'hk':'Hong Kong', 'hn':'Honduras', 'hu':'Hungary', 'id':'Indonesia', 'ie':'Ireland', 'is':'Iceland', 'it':'Italy', 'jp':'Japan', 'lt':'Lithuania', 'lu':'Luxembourg', 'lv':'Latvia', 'mx':'Mexico', 'my':'Malaysia', 'nl':'Netherlands', 'no':'Norway', 'nz':'New Zealand', 'pa':'Panama', 'pe':'Peru', 'ph':'Philippines', 'pl':'Poland', 'pt':'Portugal', 'py':'Paraguay', 'se':'Sweden', 'sg':'Singapore', 'sk':'Slovakia', 'sv':'El Salvador', 'tr':'Turkey', 'tw':'Taiwan', 'us':'US', 'uy':'Uruguay'}

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


app.after_request(add_cors_headers)


@app.route('/', methods=['GET'])
def index():
    return "Hello! This is the home page."


@app.route('/get-data', methods=['GET'])
def get_data():
    db_file = 'data.db' # Replace with the actual file path
    date_filter = request.args.get('date', '2017-01-01')
    region = request.args.get('region', 'ec')
    if region in region_map:
        region_filter = region
    else:
        region_filter = [k for k, v in region_map.items() if v == region][0]
    top_n = 10

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)

    # Query the data
    query = f"""
        SELECT *
        FROM data
        WHERE Region = '{region_filter}' AND Date = '{date_filter}'
        LIMIT {top_n}
    """
    # WHERE Region = '{region_filter}' AND Date = '{date_filter}'
    df_filtered = pd.read_sql_query(query, conn)
    print("df_filtered", df_filtered)

    # Close the connection to the SQLite database
    conn.close()

    # Convert to JSON and return the result
    result = df_filtered.to_dict(orient='records')
    response = make_response(jsonify(result))
    return response

@app.route('/get-regions', methods=['GET'])
def get_regions():
    db_file = 'data.db'

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)

    # Read the data and find the unique regions
    df = pd.read_sql_query('SELECT DISTINCT Region FROM data ORDER BY Region ASC', conn)

    # Close the connection to the SQLite database
    conn.close()
    data = [region_map[r] for r in df['Region'].tolist()]
    # Convert to JSON and return the result
    response = make_response(jsonify(data))
    return response

@app.route('/get-dates', methods=['GET'])
def get_dates():
    db_file = 'data.db'

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)

    # Read the data and find the unique dates
    df = pd.read_sql_query('SELECT DISTINCT Date FROM data ORDER BY Date ASC', conn)

    # Close the connection to the SQLite database
    conn.close()

    # Convert to JSON and return the result
    response = make_response(jsonify(df['Date'].tolist()))
    return response

@app.route('/get-lyrics', methods=['GET'])
def get_lyrics():
    date_filter = request.args.get('date', '2017-01-01')
    region = request.args.get('region', 'ec')
    if region in region_map:
        region_filter = region
    else:
        region_filter = [k for k, v in region_map.items() if v == region][0]
    top_n = 20
    db_file = 'data.db'

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)

    # Read the data and filter it
    df = pd.read_sql_query('SELECT * FROM data WHERE Date = ? AND Region = ?', conn, params=[date_filter, region_filter])

    # Close the connection to the SQLite database
    conn.close()

    df_filtered = df.nlargest(min(top_n, df.shape[0]), 'Streams')
    track_name = df_filtered["Track Name"].to_numpy()
    artist = df_filtered["Artist"].to_numpy()

    musix = Musixmatch(track_name, artist)
    word_list, word_count = musix.word_appearance()
    result = {"words": word_list, "word_count_obj": word_count, "size": df_filtered.shape}
    response = make_response(jsonify(result))
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
