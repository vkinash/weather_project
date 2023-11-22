
<h3>Setup</h3>
<li>Install python 3.10+: https://www.python.org/downloads/</li>
<li>Clone project</li>
<li>In the root project directory execute 'python -m venv venv'</li>
<li>Activate virtual environment (venv): source venv/bin/activate</li>
<li>Execute 'pip install requirements.txt'</li>
<li>In the root project directory execute 'python run.py'</li>

<h3>Project structure</h3>

* weather_project # root directory
  * scheduler_app 
    * services.py # all API's connections needed for collecting data from third party API
      * openweathermap.py # all requests to openweathermap API
    * tasks.py # tasks that will execute in the scheduler 
  * weather_api
    * routes.py # all endpoints (in this case one endpoint for collecting weather data)
    * schemas.py * schemas of response and request to endpoint
  * .env.example # example of .env file
  * config.py # class for setting up configuration from .env if it's provided. If .env doesn't exist, default configuration from Settings class will be used
  * database.py # SQLAlchemy configuration
  * dependencies.py # fastapi dependencies injections function. In this case token validation
  * models.py # database models.
  * requirements.txt # describes python dependencies
  * run.py # main project setting for executing project (project initialization, database creating, endpoints register etc.)
  * utils.py # database connection context manager

<h3>Notes</h3>
<li>If the search is performed by city name the program select the first city from the list returned by the geolocation API.
In case when you need city weather by city name and there are several cities in the world with the same name
you should use 'latitude' and 'longitude' in the config. if the config contains latitude, longitude AND city name
the search will be carried out only by latitude and longitude.</li>
<li>OpenAPI docs you can find by the link http://127.0.0.1:8000/docs</li>

<h3>Possible improvements</h3>
<li>Split the weather_api and scheduler_app into two different project</li>
<li>For task scheduling use RQ Scheduler or Celery. Now the project use repeat_every decorator from fastapi_utils.tasks module</li>
<li>Instead of using SQLite, use a different database and date partitioned data. This will help with data access if the project
will work for a long time. </li>
<li>Adding logging</li>
<li>Adding tests</li>

