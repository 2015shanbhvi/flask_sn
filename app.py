from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

#create server object
app = Flask(__name__)

#for security, cross-site scripting
CORS(app)

#routes == endpoints
#unique endpoints
#server decides what data to send
#endpoint examples: login, etc...
@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'GET':
		pass

	if request.method == 'POST':
		name = request.form.get('name')
		post = request.form.get('post')
		create_post(name, post)

	posts = get_posts()

	#rerender template any time we get new posts
	#tempalte will access posts passed in
	return render_template('index.html', posts=posts)

#if this file is selected to run
if __name__ == '__main__':
	app.run(debug=True)
