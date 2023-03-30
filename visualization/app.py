from flask import Flask, jsonify, make_response, request
import pandas as pd

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
    csv_file = 'data.csv'
    date_filter = '2017-01-01'
    region_filter = request.args.get('region', 'ec')
    top_n = 10

    # Read and filter the data
    df = pd.read_csv(csv_file, parse_dates=['Date'])
    df_filtered = df[(df['Region'] == region_filter) & (df['Date'] == date_filter)]
    df_filtered = df_filtered.nlargest(top_n, 'Streams')

    # Convert to JSON and return the result
    result = df_filtered.to_dict(orient='records')
    response = make_response(jsonify(result))
    return response

@app.route('/get-regions', methods=['GET'])
def get_regions():
    csv_file = 'data.csv'  # Replace with the actual file path

    # Read the data and find the unique regions
    df = pd.read_csv(csv_file)
    unique_regions = df['Region'].unique()

    # Convert to JSON and return the result
    response = make_response(jsonify(unique_regions.tolist()))
    return response


if __name__ == '__main__':
    app.run(debug=True)
