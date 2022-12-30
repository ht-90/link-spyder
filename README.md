# link-spyder
crawl website and build link relationship viz

## Setup

1. Install Docker
2. Set environmental variables
3. Create .env file and directories

### Install Docker

Docker needs to be installed to build a development environment.

### Set environmental variables

`>>> export PROJECT_ENV=development`

Docker-compose.yml reads this env variable and locates .env file

### Create .env file and directories

Create folders and file in the following structure/names

`./.env/PROJECT_ENV/.env`

PROJECT_ENV needs to be replaced by the value of environmental variable (i.e. development).

Example:

`./.env/development/.env`, and the .env file contains below

```
# .env file
SECRET_KEY=jB-fy!1ewhU70Jd_b
DEBUG=0
```

## How to Use Link-Spyder

* Build and start a docker-container by `>>> docker-container up`
* Open `localhost:8000` on a browser for local development
* Enter a URL of a website's sitemap in a search box and click a button next to it
* The app will scrape website pages and internal link information, then create a graph visualisation and key statistics of the website

Note:

* URL must be for sitemap (i.e. https://website.com/sitemap.xml)
* Currently limited to the sites which has sitemap in xml format

## CI/CD

CI/CD is set up for local development and github actions (by branch) for the following tasks:

* Local Development (`>>> tox`)
  * lint
  * test
* Github Actions - develop branch (pushing commit)
  * lint
  * test
* Github Actions - main branch (pushing commit)
  * lint
  * test
  * deployment

*NOTE: REQUIRE UPDATE TO BE EXECUTED IN DOCKER CONTAINER FOR LOCAL DEVELOPMENT*

## Dependencies

* django
* urllib
* beautifulsoup4
* numpy
* [d3-force](https://github.com/d3/d3-force)
