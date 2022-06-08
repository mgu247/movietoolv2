#import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

#def get_db_connection():
#    conn = sqlite3.connect('database.db')
#    conn.row_factory = sqlite3.Row
#    return conn

#def get_post(post_id):
#    conn = get_db_connection()
#    post = conn.execute('SELECT * FROM posts WHERE id = ?',
#                        (post_id,)).fetchone()
#    conn.close()
#    if post is None:
#        abort(404)
#    return post

@app.route('/')
def index():
    #conn = get_db_connection()
    #posts = conn.execute('SELECT * FROM posts').fetchall()
    #conn.close()
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
