from ext import app
from flask import Flask, jsonify, render_template
import requests
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lists', methods=['GET'])
def get_lists():
    try:
        response = requests.get('https://csfloat.com/api/v1/listings?page=60')
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
