from flask import Flask, Response
from trie import Trie
import json
import sys

app = Flask(__name__, static_url_path='')
name_trie = Trie()

def init_autocomplete(names):
    for name in names:
        name_trie.insert(name)

@app.route('/autocomplete/<prefix>')
def autocomplete(prefix):
    return Response(json.dumps(name_trie.autocomplete(prefix)),\
                mimetype='application/json')

@app.route('/')
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    names = open(sys.argv[1]).readlines()
    init_autocomplete(map(lambda x: x.strip(), names))

    app.run()
