# pa-state-park-weather-app

My wife and I enjoy hiking and camping. However, we do not like spending our weekends outside in rainy weather. We live in Pennsylvania.
My wife was recently looking for a state parks to visit, but was concerned about the chance of rain. And so began her manual search for pennsylvania state parks
and the weather forecast at each location, most importantly, the chance of rain. This little web app is to make it much easier to enjoy weekends outside in the Fall without wasting so much time manually checking weather forecasts.

# Solution
* Established a MongoDB Atlas collection storing the name of each Pennsylvania state park along with it's latitude and longitude coordinates.
* Maintain a separate script that calls to a forecast api on openweathermap (https://openweathermap.org/api/one-call-api) to get the 7 day forecast and sets forecast information for each Park within my MongoDB collection.
* Developed a Flask app and host it on Heroku to display the 7 day forecast (starting with % chance of rain) across all Pennsylvania state parks.
* Plan to learn more about front end styling and incrementally improve the presentation of the information.

# Web App Location
https://pa-state-park-weather-app.herokuapp.com/
