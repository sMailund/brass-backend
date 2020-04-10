import datetime
from google.cloud import datastore

from flask import Flask, jsonify, request

datastore_client = datastore.Client()

app = Flask(__name__)

# TODO: error handling
def get_task(task_number):
    query = datastore_client.query(kind='task').add_filter('task_number', '=', int(task_number))
    result = list(query.fetch())

    return result[0]

@app.route('/task/<task_number>', methods=['GET'])
def get(task_number):
    result = get_task(task_number)
    return jsonify(result), 200

@app.route('/task/<task_number>', methods=['PATCH'])
def patch(task_number):
    task = get_task(task_number)
    reset = request.form.get('reset')
    if reset:
        task['solved'] = False
        return task, 200
    answer = request.form.get('answer').strip().lower()
    if (task['solution']) == answer:
        task['solved'] = True
        datastore_client.put(task)
        return jsonify(task), 200
    else:
        return jsonify(task), 400 # TODO: is there a cleaner rest way to do this?

@app.route('/task/', methods=['GET'])
def list_tasks():
    query = datastore_client.query(kind='task')
    query.order = ['task_number']
    result = list(query.fetch())
    return jsonify(result), 200

@app.route('/task/', methods=['PATCH'])
def reset_tasks():
    query = datastore_client.query(kind='task')
    query.order = ['task_number']
    result = list(query.fetch())
    for task in result:
        task['solved'] = False
    datastore_client.put_multi(result)
    return jsonify(result), 200



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=True)
