import mysql.connector
from flask import Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)

# Connect to the database
db = mysql.connector.connect(
    host="aisha-aws-db1.cvdxeitqk2c8.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Codeforcode",
    database="nutritionappdb"
)

cursor = db.cursor()


def insert_data():
    cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)",
                   ("yash", "27"))

    db.commit()
