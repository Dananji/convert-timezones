### Description

This is a simple application that shows the current time of a given timezone.
To do this the application uses a Python Flask back-end with a Vue.js client.

### Run on local machine

- Get a copy of the project on your local machine with, `git clone https://github.com/Dananji/convert-timezones.git`
- Open up a terminal from the root directory of the project and run the following:
    ```
    cd server
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python main.py
    ```
    This will start the server at port 5000 in your localhost, but the root path will not serve anything. This will serve 2 endpoints:
    1. `/timezones` : gives a list of timezones using Python's `pytz` package
    2. `/time?timezone=<timezone>` : calculates the current time of the given timezone

- In another terminal window;
    ```
    cd client
    npm install
    npm run serve
    ```
    Navigate to http://localhost:8080 to see the application running in your browser.