# pse-indices-scoreboard
This Django app uses Scrapy, Celery, and Redis to collect, store, and display updated values of the 8 main indices of the Philippine equity market. The app tries to implement the following functionalities from scratch:

* Building a Scrapy spider that replicates an ajax request
* Running a Scrapy spider in a Django app
* Wiring up Scrapy item pipelines with Django models
* Using Celery to schedule scraping tasks

While there are already numerous tested tools and packages to carry out the above tasks, I just wanted to "reinvent the wheel" a little bit to see how far I can get away with it.

## Dependencies
The main packages that make up this project include:
* Django==2.2.3
* celery==4.3.0
* redis==3.3.5
* Scrapy==1.7.2

The app uses a PostgreSQL database, so it requires `psycopg2` to be installed. Please see project's `requirements.txt` file for a complete list of dependencies.

### Environment Variables
The app expects appropriate values for the following environment variables to be set in a `.env` file:

* `DB_USERNAME`
* `DB_PASSWORD`
* `DB_NAME`
* `DB_PORT`

## Celery Beat Schedule Settings
The app's Scrapy spider is set to crawl the PSE homepage every 3 minutes from 9 a.m. to 4 p.m. (Philippine local time) from Mondays through Fridays. This can be adjusted by modifying the `CELERY_BEAT_SCHEDULE` setting under the `pse_summary/settings.py` module as follows:

```
CELERY_BEAT_SCHEDULE = {
    'get-values-during-business-hours': {
        'task': 'index_getter',
        'schedule': crontab(minute='*/5', hour='9-16', day_of_week='1-5')
    }
}
```

To achieve mor granular control over the spider's crawl schedule, please read more about crontab settings on the [Periodic Tasks](https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html) page of the Celery documentation.

## Resources
Getting Scrapy, Django, and Celery to play nice together (without other third-party packages) took me a while to figure out. That's why using packages like [django-dynamic-scraper](https://django-dynamic-scraper.readthedocs.io/) is probably a better route to take for most use-cases (though I haven't tried it out yet).

That said, the following resources helped me work around dead ends and hack this project together:

* [Using Django models in Scrapy item pipelines without DjangoItem](https://github.com/bipul21/scrapy_django)
* [ModuleNotFoundError when setting Scrapy as an app in Django](https://stackoverflow.com/questions/55236051/modulenotfounderror-when-sets-scrapy-as-an-app-in-django)
* [Getting Scrapy project settings when script is outside of root directory](https://stackoverflow.com/questions/31662797/getting-scrapy-project-settings-when-script-is-outside-of-root-directory)

## License
[MIT license](https://opensource.org/licenses/MIT)