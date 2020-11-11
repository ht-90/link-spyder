from flask import Flask, render_template, request
import json
from linkspyder.spyder import Spyder
from linkspyder.validators import URLValidator


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", viz_data=[{"": ""}])

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
            spyder.clean_extracted_urls()
            spyder.extract_valid_destination_urls()

            return render_template("index.html", viz_data=spyder.edges_list_clean), 200
        
        else:
            error_msg = f"""
                <div class="block" style="margin-top: 2.5rem;">
                  <p class="sub-title is-size-4 has-text-centered" style="font-style: italic;">
                    <span style="color: red;font-weight: 500">{url}</span> is not a valid URL...
                  </p>
                </div>
                """

            return render_template("index.html", viz_data=[{"": ""}], error_msg=error_msg)

if __name__ == '__main__':
    app.run()
