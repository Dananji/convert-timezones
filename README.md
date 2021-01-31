### Description

This is a simple application that shows the current time of a given timezone.
To do this the application uses a Python Flask back-end with a Vue.js client.

### Requirements

To run this project on your local machine you need the following installed;
- Python (at least version 3.6.9)
- Flask (1.1.2) and Flask-Cors (3.0.10)
- Vue/cli (4.5.11)

### Run on local machine

- Get a copy of the project on your local machine with `git clone https://github.com/Dananji/convert-timezones.git`
- Open up a terminal from the root directory of the project
- Go into `server`directory and run `python main.py`
    - This will start the server at http://localhost:5000 
- In another terminal window, go into `client` directory and run `npm run serve`
    - Navigate to http://localhost:8080 to see the application running in your browser