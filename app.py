# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
		
		# Heroku
    engine = create_engine("postgresql://uxweficayqkvnb:191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f@ec2-54-225-234-165.compute-1.amazonaws.com:5432/ddtk33j69v200c", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS iris(
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )
    data = pd.read_csv('data/iris.csv')
    print(data)
    data.to_sql(name='iris', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "Hello World!"



if __name__ == "__main__":
    db_create()
    app.run()