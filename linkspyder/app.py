from flask import Flask, render_template, request
import json
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
        url = request.get_data().decode('utf8')
        # Create a validator for a user input URL
        url_is_valid = URLValidator(url=url)

        if url_is_valid():
            # Crawl the URL page
            # spyder = Spyder(url=url)
            # spyder.initial_crawl()
            # spyder.deep_crawl()
            # spyder.clean_scraped_data()
            # spyder.generate_nodes_links()
            # viz_data = spyder.generate_graph_data()
            viz_data = {
                "nodes": [
                    {
                        "id": "info.yahoo.com.au",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/topics/coronavirus",
                        "source_category": 1
                    },
                    {
                        "id": "au.tv.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "source_category": 1
                    },
                    {
                        "id": "au.news.yahoo.com/weather/australia/queensland/brisbane-1100661",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "source_category": 1
                    },
                    {
                        "id": "au.finance.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "source_category": 1
                    },
                    {
                        "id": "au.lifestyle.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "source_category": 1
                    },
                    {
                        "id": "au.sports.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "source_category": 1
                    },
                    {
                        "id": "au.tv.yahoo.com/au-news-video-national-playlist-new",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "source_category": 1
                    },
                    {
                        "id": "au.news.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/everything",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/topics/latest-au",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "source_category": 1
                    },
                    {
                        "id": "au.tv.yahoo.com/au-news-video-national-playlist-new/trump-appears-almost-accept-lost-223305438",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/topics/latest-au",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/topics",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/account/preferences",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/topics",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/topics/latest-au",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/topics",
                        "source_category": 1
                    },
                    {
                        "id": "au.news.yahoo.com/weather",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/topics/us-election",
                        "source_category": 1
                    },
                    {
                        "id": "help.yahoo.com/au",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/topics/latest-au",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/topics",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "source_category": 1
                    },
                    {
                        "id": "au.lifestyle.yahoo.com/entertainment",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "source_category": 1
                    },
                    {
                        "id": "safety.yahoo.com/AU",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "source_category": 1
                    },
                    {
                        "id": "yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "login.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "mail.yahoo.com",
                        "source_category": 1
                    },
                    {
                        "id": "au.yahoo.com/topics/coronavirus",
                        "source_category": 1
                    }
                ],
                "links": [
                    {
                        "source": "yahoo.com",
                        "target": "info.yahoo.com.au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/topics/coronavirus",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.tv.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.news.yahoo.com/weather/australia/queensland/brisbane-1100661",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.finance.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.lifestyle.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.sports.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.news.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/everything",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new/trump-appears-almost-accept-lost-223305438",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/account/preferences",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.news.yahoo.com/weather",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/topics/us-election",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "help.yahoo.com/au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.lifestyle.yahoo.com/entertainment",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "mail.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "safety.yahoo.com/AU",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "login.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "yahoo.com",
                        "target": "au.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "info.yahoo.com.au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/topics/coronavirus",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.tv.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.news.yahoo.com/weather/australia/queensland/brisbane-1100661",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.finance.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.lifestyle.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.sports.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.news.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/everything",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new/trump-appears-almost-accept-lost-223305438",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/account/preferences",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.news.yahoo.com/weather",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/topics/us-election",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "help.yahoo.com/au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.lifestyle.yahoo.com/entertainment",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "mail.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "safety.yahoo.com/AU",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "login.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com",
                        "target": "au.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "info.yahoo.com.au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/topics/coronavirus",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.tv.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.news.yahoo.com/weather/australia/queensland/brisbane-1100661",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.finance.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.lifestyle.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.sports.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.news.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/everything",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new/trump-appears-almost-accept-lost-223305438",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/account/preferences",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.news.yahoo.com/weather",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/topics/us-election",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "help.yahoo.com/au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.lifestyle.yahoo.com/entertainment",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "mail.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "safety.yahoo.com/AU",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "login.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "login.yahoo.com",
                        "target": "au.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "info.yahoo.com.au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/topics/coronavirus",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.tv.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.news.yahoo.com/weather/australia/queensland/brisbane-1100661",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.finance.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.lifestyle.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.sports.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.news.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/everything",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new/trump-appears-almost-accept-lost-223305438",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/account/preferences",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.news.yahoo.com/weather",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/topics/us-election",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "help.yahoo.com/au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.lifestyle.yahoo.com/entertainment",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "mail.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "safety.yahoo.com/AU",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "login.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "mail.yahoo.com",
                        "target": "au.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "info.yahoo.com.au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.tv.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.news.yahoo.com/weather/australia/queensland/brisbane-1100661",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.finance.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.lifestyle.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/sports/boxing-reality-star-tommy-fury-insane-knockout-005731887",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.sports.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.news.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/everything",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/wrapup-1-biden-cements-victory-053752003",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.tv.yahoo.com/au-news-video-national-playlist-new/trump-appears-almost-accept-lost-223305438",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/i-was-ashamed-work-accident-leaves-woman-covered-in-burns-010941289",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/account/preferences",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/evan-spiegel-miranda-kerr-avoid-hotel-quarantine-233131612",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.news.yahoo.com/weather",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/topics/us-election",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "help.yahoo.com/au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/no-not-reaching-trump-voters-060009511",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/trump-again-boasts-won-pennsylvania-045213959",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/dan-rather-schools-trump-reelection-195807430",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/sports/tennis-novak-djokovic-major-serena-williams-admission-031200388",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/topics/latest-au",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/trump-press-secretary-slammed-for-bizarre-lie-over-crowd-size-002024317",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/topics",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/breakthrough-finding-reveals-why-certain-covid-19-patients-die-022240688",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.lifestyle.yahoo.com/entertainment",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/sports/the-masters-paige-spiranac-mocks-bryson-dechambeau-211703280",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "mail.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/ex-trump-org-exec-warns-084426552",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/protesters-storm-hotel-after-trump-rally-turns-violent-033825845",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "safety.yahoo.com/AU",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/retired-4-star-general-alarmed-033237179",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/donald-trumps-slip-tongue-suggests-221948304",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/trump-hopes-fade-biden-wins-arizona-183055206--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/new-theory-emerges-on-why-trump-wont-accept-election-loss-232730733",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "login.yahoo.com/news/trump-told-hell-thing-friend-193450466--spt",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "yahoo.com/news/kim-jongun-sparks-fears-of-secret-plot-as-he-mysteriously-disappears-234803088",
                        "value": 1,
                        "source_category": 1
                    },
                    {
                        "source": "au.yahoo.com/topics/coronavirus",
                        "target": "au.yahoo.com/news/mega-crocodile-weighing-almost-a-tonne-caught-in-drain-system-050320169",
                        "value": 1,
                        "source_category": 1
                    }
                ]
            }
            return json.dumps(viz_data)
        
        else:
            error_msg = f"""
                <div class="block" style="margin-top: 2.5rem;">
                  <p class="sub-title is-size-4 has-text-centered" style="font-style: italic;">
                    <span style="color: red;font-weight: 500">{url}</span> is not a valid URL...
                  </p>
                </div>
                """

            return render_template("index.html", error_msg=error_msg)

if __name__ == '__main__':
    app.run()
