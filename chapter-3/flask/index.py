#!/usr/bin/env python
from pymongo import Connection
import json
from flask import Flask, render_template


app = Flask(__name__)
connection = Connection()
db = connection.agile_data




@app.route("/<input>")
def echo(input):
    return input

@app.route("/sent_counts/<ego1>/<ego2>")
def sent_counts(ego1, ego2):

    find_search_result = db.sent_counts.find_one({'from': ego1, 'to': ego2})
    data = {}

    data['keys'] = '_id', 'from', 'to', 'total'
    data['values'] = find_search_result['_id'], find_search_result['from'], find_search_result['to'], find_search_result['total']
    return render_template('table.html', data=data)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0')
