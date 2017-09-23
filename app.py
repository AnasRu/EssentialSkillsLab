#!flask/bin/python

from flask import Flask, abort
from flask.helpers import make_response
from flask.json import jsonify
from flask import request
app = Flask(__name__)

tasks = [{'id':1,
          'title':u'Buy groceries',
          'description':'Milk,Cheese',
          'done':False},{'id':2,
             'title':'write report',
             'description':"write report of Essential skills",
              'done':False}]



@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['GET'])
def get_task_by_id(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response((jsonify({'error':'Not found'}),404))

@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def add_task():
    if ( not request.json or 'title' not in request.json):
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({'task':task}),201



def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)