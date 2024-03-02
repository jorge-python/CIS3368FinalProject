# http://127.0.0.1:5000/api/facility
# http://127.0.0.1:5000/api/classroom
# http://127.0.0.1:5000/api/teacher
# http://127.0.0.1:5000/api/child

import flask
from flask import jsonify, request
from sql import create_connection, execute_read_query, execute_query
import creds

# setting up an application name
app = flask.Flask(__name__) # sets up the application
app.config["DEBUG"] = True # allow to show errors in browser

myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)


# API's for 'facility' table
@app.route('/api/facility', methods=['GET'])
def view_all_facilities():
    sql = "SELECT * FROM facility"
    query = execute_read_query(conn, sql)
    results = []
    for result in query:
        results.append(result)
    return jsonify(results)
#@app.route('/api/facility', methods=['POST'])
#@app.route('/api/facility', methods=['PUT'])
#@app.route('/api/facility', methods=['DELETE'])



# API's for 'classroom' table
@app.route('/api/classroom', methods=['GET'])
def view_all_classrooms():
    sql = "SELECT * FROM classroom"
    query = execute_read_query(conn, sql)
    results = []
    for result in query:
        results.append(result)
    return jsonify(results)
#@app.route('/api/classroom', methods=['POST'])
#@app.route('/api/classroom', methods=['PUT'])
#@app.route('/api/classroom', methods=['DELETE'])



# API's for 'teacher' table
@app.route('/api/teacher', methods=['GET'])
def view_all_teachers():
    sql = "SELECT * FROM teacher"
    query = execute_read_query(conn, sql)
    results = []
    for result in query:
        results.append(result)
    return jsonify(results)
#@app.route('/api/teacher', methods=['POST'])
#@app.route('/api/teacher', methods=['PUT'])
#@app.route('/api/teacher', methods=['DELETE'])



# API's for 'child' table
@app.route('/api/child', methods=['GET'])
def view_all_children():
    sql = "SELECT * FROM child"
    query = execute_read_query(conn, sql)
    results = []
    for result in query:
        results.append(result)
    return jsonify(results)
#@app.route('/api/child', methods=['POST'])
#@app.route('/api/child', methods=['PUT'])
#@app.route('/api/child', methods=['DELETE'])



app.run()