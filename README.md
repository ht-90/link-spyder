# link-spyder
crawl website and build link relationship viz


# Get started

* Windows

```shell
>>> cd linkspyder
>>> set FLASK_ENV=development
>>> flask run
```

*FLASK_ENV=development to execute in development mode*


# Dependencies

* flask
* urllib
* beautifulsoup4
* [d3-force](https://github.com/d3/d3-force)

# Docker container


* Create and start a docker container: `$ docker-compose up -d --build`
* Start bash: `$ docker-compose exec link-spyder bash`
* Remove a container: `$ docker-compose down`
