from flask import Flask, render_template, request
from linkspyder.spyder import Spyder


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def data():
    if request.method == "POST":
        # Receive user input URL
        url = request.form["input-url"]

        # Crawl the URL page
        spyder = Spyder(url=url)
        spyder.initial_crawl()
        spyder.deep_crawl()
        # Create web viz
        web_viz = spyder.create_web()
        
        return render_template("index.html", web_viz=web_viz), 200
