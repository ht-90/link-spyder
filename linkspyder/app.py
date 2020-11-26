from flask import Flask, render_template, request, jsonify
from linkspyder.spyder import Spyder
from linkspyder.validators import URLValidator


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data", methods=["POST"])
def crawl():
    if request.method == "POST":
        # Receive user input URL
        url = request.get_data().decode("utf8")
        # Create a validator for a user input URL
        url_is_valid = URLValidator(url=url)

        if url_is_valid():
            # Crawl the URL page
            spyder = Spyder(url=url)
            spyder.initial_crawl()
            spyder.deep_crawl()
            spyder.generate_nodes_links()
            spyder.categorise_nodes()
            spyder.categorise_links()
            graph_data, category_data = spyder.generate_graph_data()

            return jsonify(graph=graph_data, category=category_data)

        else:
            error_msg = f"""
                <div class="block" style="margin-top: 2.5rem">
                  <p
                    class="sub-title is-size-4 has-text-centered"
                    style="font-style: italic"
                  >
                    <span
                      style="color: red; font-weight: 500"
                    >
                    {url}
                    </span> is not a valid URL...
                </p>
                </div>
                """

            return render_template("index.html", error_msg=error_msg)


if __name__ == "__main__":
    app.run()
