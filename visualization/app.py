from flask import Flask, jsonify, make_response, request
import pandas as pd
from load_lyrics import Musixmatch
import csv

app = Flask(__name__)


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
    # csv_file = 'visualization/data.csv'
    # date_filter = '2017-01-01'
    # region_filter = request.args.get('region', 'ec')
    # top_n = 10

    # # Read and filter the data
    # df = pd.read_csv(csv_file, parse_dates=['Date'])
    # df_filtered = df[(df['Region'] == region_filter) & (df['Date'] == date_filter)]
    # df_filtered = df_filtered.nlargest(top_n, 'Streams')

    # # Convert to JSON and return the result
    # result = df_filtered.to_dict(orient='records')
    # response = make_response(jsonify(result))
    # return response

    csv_file = 'visualization/data.csv'
    date_filter = '2017-01-01'
    region_filter = request.args.get('region', 'ec')
    top_n = 10

    filtered_rows = []

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_found = False

        for row in reader:
            current_date = row['Date']
            current_region = row['Region']

            if current_region == region_filter and current_date == date_filter:
                data_found = True
                filtered_rows.append(row)

                if len(filtered_rows) >= top_n:
                    break
            elif data_found:
                break

    # Convert the 'Streams' column to integer type for sorting
    for row in filtered_rows:
        row['Streams'] = int(row['Streams'])

    # Sort the filtered data and get the top N records
    filtered_rows = sorted(filtered_rows, key=lambda x: x['Streams'], reverse=True)[:top_n]

    # Convert to JSON and return the result
    response = make_response(jsonify(filtered_rows))
    return response

@app.route('/get-regions', methods=['GET'])
def get_regions():
    csv_file = 'visualization/total_stream_count.csv'

    # Read the data and find the unique regions
    df = pd.read_csv(csv_file)
    unique_regions = df['Region'].unique()

    # Convert to JSON and return the result
    response = make_response(jsonify(unique_regions.tolist()))
    return response


@app.route('/get-lyrics', methods=['GET'])
def get_lyrics():
    date_filter = '2017-01-01'
    region_filter = request.args.get('region', 'ec')
    top_n = 10
    csv_file = 'visualization/data.csv'

    df = pd.read_csv(csv_file, parse_dates=['Date'])
    df_filtered = df[(df['Region'] == region_filter) & (df['Date'] == date_filter)]
    df_filtered = df_filtered.nlargest(min(top_n, df_filtered.shape[0]), 'Streams')
    track_name = df_filtered["Track Name"].to_numpy()
    artist = df_filtered["Artist"].to_numpy()

    musix = Musixmatch(track_name, artist)
    word_list, word_count = musix.word_appearance()
    result = {"words": word_list, "word_count_obj": word_count, "size": df_filtered.shape}
    response = make_response(jsonify(result))
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
