from flask import Flask, render_template, request, jsonify
from linkspyder.spyder import Spyder
from linkspyder.sitemapspyder import SitemapSpyder
from linkspyder.analyzer import Analyzer
from linkspyder.validators import URLValidator


app = Flask(__name__)
MAX_CRAWL = 5


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
            spyder.size_nodes()
            graph_data, category_data = spyder.generate_graph_data()

            # Analyze crawled data
            analyzer = Analyzer(
                url=url,
                graph=graph_data,
                cat=category_data
            )
            stats = analyzer.generate_stats()

            print("NODES", graph_data["nodes"][:3])
            print("LINKS", graph_data["links"][:3])

            return jsonify(
                graph=graph_data,
                category=category_data,
                stats=stats
              )

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


@app.route("/sitemapper", methods=["POST"])
def crawl_sitemap():
    if request.method == "POST":
        # Receive user input URL
        url = request.get_data().decode("utf8")
        # Create a validator for a user input URL
        url_is_valid = URLValidator(url=url)

        if url_is_valid():
            sms = SitemapSpyder(url=url, max_crawl=MAX_CRAWL)
            # Get domain and sitemap of url
            domain_name = sms.retrieve_domain(url=url)
            locs_url = sms.parse_sitemap(url=url)
            # Parse urls in sitemap
            parsed_pages = sms.parse_page_threading(urls=locs_url)
            # Retrieve a tags from each page
            url_a_tags = sms.retrieve_a_tags(parsed_pages=parsed_pages)

            # Parse sitemap pages and extract hrefs as internal or external
            res_int = []
            res_ext = []

            for url_a_tag in url_a_tags:
                loc = url_a_tag[0]
                a_tags = url_a_tag[1]

                hrefs_page = [a.attrs.get("href") for a in a_tags]
                hrefs_page = [
                  sms.convert_to_absolute_url(url=url, href=href)
                  for href in hrefs_page
                ]
                hrefs_page = [
                  sms.normalize_url(url=href) for href in hrefs_page
                ]
                valid_hrefs = []
                for href in hrefs_page:
                    if (
                      sms._page_is_valid(url=href) and
                      sms._page_is_in_sitemap(url=url, sitemap_locs=locs_url)
                    ):
                        valid_hrefs.append(href)

                int_links = sms.extract_internal_links(
                  hrefs=hrefs_page, domain_name=domain_name, url=loc
                )
                ext_links = sms.extract_external_links(
                  hrefs=hrefs_page, domain_name=domain_name, url=loc
                )

                res_int.append(
                  {"source": loc, "value": 1, "target": int_links}
                )
                res_ext.append(
                  {"source": loc, "value": 1, "target": ext_links}
                )

            # Trim url scheme to hide it from UI
            locs_url = [sms.trim_url_scheme(loc) for loc in locs_url]

            # Create viz dataset
            category_data = sms.create_node_categories(locs_url)
            nodes_int = sms.create_nodes(
              sitemap_locs=locs_url, categories=category_data, url=url
            )
            edges_int = sms.create_edges(
              links=res_int, nodes=nodes_int, categories=category_data
            )
            category_data = sms.create_group_data(
              domain_name=domain_name, categories=category_data
            )
            nodes_int = sms.size_nodes(links=edges_int, nodes=nodes_int)
            graph_data = sms.generate_graph_data(
              nodes=nodes_int, edges=edges_int
            )

            print("DOMAIN:", domain_name)
            print("LEN_NODES:", len(graph_data["nodes"]))
            print("LEN_LINKS:", len(graph_data["links"]))
            print("LEN_CATEGORY:", len(category_data))

            # Analyze crawled data
            analyzer = Analyzer(
                url=url,
                graph=graph_data,
                cat=category_data
            )
            stats = analyzer.generate_stats_sitemap()

            return jsonify(
                graph=graph_data,
                category=category_data,
                stats=stats
              )

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
