from flask import Flask, Response, g, jsonify
from trie import Trie
from datetime import datetime
import json
import sys
import sqlite3

app = Flask(__name__, static_url_path='')
name_trie = Trie()
DATABASE = './users.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.commit()
        db.close()

def init_autocomplete(names):
    for name in names:
        name_trie.insert(name)

@app.route('/autocomplete/<prefix>')
def autocomplete(prefix):
    return Response(json.dumps(name_trie.autocomplete(prefix)),\
                mimetype='application/json')

@app.route('/checkin/<name>/<shirt_size>')
def checkin(name, shirt_size):
    result = query_db(
        "select checked_in, checked_in_at from users where name = ?", (name,))
    if len(result) == 0:
        return jsonify(success=False, message="User in not in first year CS")


    checked_in, checked_in_at = result[0]
    if bool(checked_in):
        return jsonify(
            success=False, message="User already checked in at " + checked_in_at)

    query_db("update users set checked_in = ?, checked_in_at = ?, shirt_size = ? where name = ?",
                (True, str(datetime.now()), shirt_size, name))
    return jsonify(success=True, message=name + " successfully checked in")

@app.route('/')
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    names = open(sys.argv[1]).readlines()
    init_autocomplete(map(lambda x: x.strip(), names))
    app.run()
