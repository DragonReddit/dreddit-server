from flask import Flask, render_template, send_from_directory
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
	return 'Endpoint not working'

#Endpoints
@app.route('/login')
def login():
	return render_template("/login/index.html")

@app.route('/status')
def platform_status():
	return render_template("/status-page/index.html")

# Blocked requests
@app.route('/api')
def blocked():
	return 'Method not allowed, sorry'

# API
@app.route('/api/login', methods = ['GET', 'POST'])
def api_login():
	return 'API Not Avialable', 503

app.run(debug = True, port = 7001)