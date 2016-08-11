from flask import Flask
app = Flask(__name__, static_url_path='')

# Keep it in memory.
index_page = open("index.html").read()

@app.route('/')
def index():
    return index_page

if __name__ == "__main__":
    app.run()
