from flask import Flask, render_template, request, jsonify, abort
from scrape import get_weather_info,get_weather_info_using_station_id
from werkzeug.middleware.proxy_fix import ProxyFix
from citylist import cities
import json

app = Flask(__name__, static_url_path="/s")
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def initiator():
    return render_template("index.html", cities=cities)

@app.route("/api")
def api():
    with open("station_ids.json","r") as f:
        return jsonify(json.load(f))

@app.route("/api/id", methods=["POST"])
def api_using_id():
    if not request.json or 'station_id' not in request.json:
        abort(400)
    station_id = request.json["station_id"]

    return jsonify(get_weather_info_using_station_id(station_id))

@app.route("/api/name", methods=["POST"])
def api_using_station_name():
    if not request.json or 'station' not in request.json:
        abort(400)
    station_name = request.json["station"]

    return jsonify(get_weather_info(station_name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)