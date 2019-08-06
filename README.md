# pse-indices-scoreboard
This Django app uses Scrapy, Celery, and Redis to collect, store, and display updated values of the 8 main indices of the Philippine equity market. The app implements the following functionalities from scratch:

* Building a Scrapy spider that replicates an ajax request
* Running a Scrapy spider in a Django app
* Wiring up Scrapy item pipelines with Django models
* Using Celery to schedule scraping tasks (in progress)

While there are already numerous tested tools and packages to carry out the above tasks, I just wanted to "reinvent the wheel" a little bit to see how far I can get away with it.

## Dependencies
The main packages that make up this project include:
* Django==2.2.3
* celery==4.3.0
* redis==3.3.5
* Scrapy==1.7.2

Please see project's `requirements.txt` file for a complete list of dependencies.

## License
[MIT license](https://opensource.org/licenses/MIT)