'''
Created on 14.01.2024

@author: neumann
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f'''
<h1>Sort Part Finder</h1>
'''
