from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .sitemapspyder import SitemapSpyder
from .analyzer import Analyzer
from .validators import SitemapURLValidator

class Index(TemplateView):
    template_name = "index.html"


@csrf_exempt
def crawl_sitemap(request):

    if request.method == "POST":

        # Receive user input URL
        url = request.body.decode("utf8")

        # Create a validator for a user input URL
        url_is_valid = SitemapURLValidator(address=url)

        if url_is_valid():

            MAX_CRAWL = 5

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

            return JsonResponse(
                {
                    "graph": graph_data,
                    "category": category_data,
                    "stats": stats,
                }
            )

        else:
            error_msg = """
                <div class="block" style="margin-top: 2.5rem">
                  <p
                    class="sub-title is-size-4 has-text-centered"
                    style="font-style: italic"
                  >
                    URL is not a valid URL...
                  </p>
                </div>
                """

            return render(request, "_sitemap_form.html", {"error_msg": error_msg})

    else:
        return redirect("index")
