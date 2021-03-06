import urllib3
import flask
import unittest
import pytest
import requests
from flask_mysqldb import MySQL
from flask import Flask
import os
import csv

app = Flask(__name__)


app.config["MYSQL_HOST"] = os.environ['MYSQL']
app.config["MYSQL_USER"] = os.environ['USER']
app.config["MYSQL_PASSWORD"] = os.environ['PASSWORD']
app.config["MYSQL_DB"] = os.environ['DATABASE']

mysql = MySQL(app)


def test_service():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost/')
    assert 200 == r.status

def test_getresponse():
    r = requests.get('http://localhost/')
    assert isinstance(r.text, str)

def test_home_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/')
    assert 200 == r.status

def test_submittheme_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/submittheme/')
    assert 200 == r.status
    
def test_aboutus_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/about')
    assert 200 == r.status
    
def test_contactus_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.197.228.70/contact')
    assert 404 == r.status

def test_home_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.125.202/')
    assert 200 == r.status
    
def test_submittheme_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.125.202/submittheme/')
    assert 200 == r.status
    
def test_aboutus_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.125.202/about')
    assert 200 == r.status
    
def test_contactus_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.125.202/contact')
    assert 404 == r.status

def test_getresponse_worker():
    r = requests.get('http://35.246.125.202/')
    assert isinstance(r.text, str)

def test_csv_service_2():
    for row in open("/home/Admin/Docker-SFIA-2/SFIA-2/service_2/application/colour.txt"):
        coloumnlist = str(row)
        coloumnlist = coloumnlist.split(",")
    assert len(coloumnlist) == 8

def test_db_insert_user():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("INSERT INTO USER (first_name, second_name,username, email,message) VALUES ('Mohammed','Zaheer','MZaheer','mzaheer@gmail.com','have mickey mouse theme')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 

def test_db_insert_theme():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("INSERT INTO themesentence (theme_sentence) VALUES ('Your Outfit colour is Black and the theme is BBQ Party in Olympus. Your Ticket price is £11')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 

def test_db_delete_user():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("DELETE FROM USER WHERE username = ('MZaheer')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 


def test_db_select():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM USER")
        mysql.connection.commit()         
        cur.close()
        assert 7 == num_of_records 