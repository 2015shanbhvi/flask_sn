import sqlite3

#do "pathing"
#layer that contains info for server <--> database
#get dir name, get file path of whatever we pass in
ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
	#conenct to database
	con = sql.connect(path.join(ROOT, 'database.db'))
	cur = con.cursor()
	#execute the sql statement
	cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
	con.commit()
	con.close()

#pull the posts we want from database
def get_posts():
	con = sql.connect(pat.join(ROOT, 'database.db'))
	cur = con.cursor
	cur.execute('select * from posts')
	posts = cur.fetchall()
	return posts




