from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.json import jsonify
import mysql.connector
from model.Campus import Campus

conn = mysql.connector.connect(user='dev', password='Ufop4&2021',
                              host='127.0.0.1',
                              database='mydbpaem')

campus = Campus(conn)

app = Flask(__name__)
api = Api(app)

api.add_resource(campus.get(), '/campus') # Route_1
app.run(port='5002')