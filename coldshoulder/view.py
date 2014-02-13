from flask import (g, session, request, url_for, flash, redirect,
                   render_template)
from coldshoulder import app

@app.route('/')
def index():
    return render_template('index.html')
