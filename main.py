import datetime
from google.cloud import datastore

from flask import Flask, jsonify

datastore_client = datastore.Client()

app = Flask(__name__)


@app.route('/task')
def get():
    query = datastore_client.query(kind='task')#.add_filter("task_number", "=", "1")
    result = list(query.fetch())

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=True)
