from flask import Flask, jsonify, request
from flask_cors import CORS
import pytz
from datetime import datetime

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS for cross-origin requests
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/timezones", methods=['GET'])
def list_timezones():
    timezones = pytz.all_timezones
    ids = list(range(0, len(timezones)))
    key_list = ['name','id']
    timezones_list = [{key_list[0]:a, key_list[1]:b} for a, b in zip(timezones, ids)]
    return jsonify(timezones_list)

@app.route("/time")
def get_time():
    timezone = request.args.get('timezone')
    format = '%Y-%m-%d %H:%M:%S %Z%z'
    current_time = pytz.timezone(timezone).localize(datetime.now())
    return jsonify(current_time.strftime(format))

if __name__ == "__main__":
    app.run()