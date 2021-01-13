from database import Database
from flask import Flask, request, make_response, redirect, url_for, render_template, session
import random
from config import Config
from cas import CASClient
from user import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
import time
import numpy as np

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    html = render_template('home.html')
    response = make_response(html)
    return response

@app.route('/poly', methods=['GET'])
def home():
    html = render_template('poly.html')
    response = make_response(html)
    return response

@app.route('/hybrid', methods=['GET'])
def home():
    html = render_template('hybrid.html')
    response = make_response(html)
    return response

@app.route('/multi', methods=['GET'])
def home():
    html = render_template('multi.html')
    response = make_response(html)
    return response

@app.route('/overgrips', methods=['GET'])
def home():
    html = render_template('overgrips.html')
    response = make_response(html)
    return response

@app.route('/strats', methods=['GET'])
def home():
    html = render_template('strats.html')
    response = make_response(html)
    return response

@app.route('/st', methods=['GET'])
def home():
    html = render_template('st.html')
    response = make_response(html)
    return response

@app.route('/about', methods=['GET'])
def home():
    html = render_template('about.html')
    response = make_response(html)
    return response