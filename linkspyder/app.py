from flask import Flask, render_template, request
from linkspyder.spyder import Spyder
from linkspyder.validators import URLValidator


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def data():
    if request.method == "POST":
        # Receive user input URL
        url = request.form["input-url"]
        # Create a validator for a user input URL
        url_is_valid = URLValidator(url=url)

        if url_is_valid():
            # Crawl the URL page
            spyder = Spyder(url=url)
            spyder.initial_crawl()
            spyder.deep_crawl()

            # Create web viz
            web_viz = spyder.create_web()

            return render_template("index.html", web_viz=web_viz), 200
        
        else:
            error_msg = f"""
                <div class="block" style="margin-top: 2.5rem;">
                  <p class="sub-title is-size-4 has-text-centered" style="font-style: italic;">
                    <span style="color: red;font-weight: 500">{url}</span> is not a valid URL...
                  </p>
                </div>
                """

            return render_template("index.html", error_msg=error_msg)
