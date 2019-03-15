from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello, World'


'''
@app.route('/user/<username>')
def show_user_profile(username):
	# show user profile for user
	return 'User %s' % username

@app.route('/post/<int:post_id')
def show_post(post_id):
	# show post with given id (int)
	return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	# show the subpath after /path/
	return 'Subpath %s' % subpath
'''
