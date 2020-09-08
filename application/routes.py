from application import app, db
from flask import json, render_template

@app.route("/")
@app.route("/index")
def index():
    return "<h1>HELLO WORLD!</h1>"

#class Park(db.Document):
@app.route("/db")
def db_info():
    
    documents = db.Park.find().sort("distance", 1)

    example = db.Park.find_one({'name' : 'Archbald Pothole State Park'})

    date_headers = []

    chances_of_rain_list_of_lists = []

    park_names = []

    example_forecast_dicts = example['daily_forecast']

    date_headers = [forecast['date'] for forecast in example_forecast_dicts]

    for document in documents:
        park_names.append(document['name'])
        forecast_dicts = document['daily_forecast']
        park_forecasts = []
        for forecast in forecast_dicts:
            chance_of_rain = str(forecast['chance_of_precipitation'])
            if len(chance_of_rain) > 1:
                chance_of_rain = chance_of_rain[1:]
            park_forecasts.append(chance_of_rain)
        chances_of_rain_list_of_lists.append(park_forecasts)

    return render_template("park_weather.html", chances_of_rain_list_of_lists=chances_of_rain_list_of_lists, 
                            park_names=park_names, date_headers=date_headers)
