import requests

city = requests.get("https://ipinfo.io/city")
data = requests.get("https://wttr.in/" + str(city) + "?format=3")
temp = int(data.text.split(" ")[4][:2])

top = ""
middle = ""
bottom = ""
if temp <= -20:
    top = "🥶🧣"
    middle = "🧥🧤"
    bottom = "🧦🎿"
elif temp < -15 and temp > -20:
    top = "🧢🧣"
    middle = "🧥"
    bottom = "👖"
elif temp < 0 and temp > -15:
    top = "🧣"
    middle = "🧥"
    bottom = "👖"
elif temp < 10 and temp > 0:
    top = "🧢"
    middle = "🧥"
    bottom = "👖"
elif temp < 15 and temp > 10:
    top = "🧢"
    middle = "👕"
    bottom = "👖"
elif temp < 20 and temp > 15:
    top = "🕶️"
    middle = "👕"
    bottom = "🩳"
elif temp >= 20:
    top = "🕶️🍦"
    middle = "👕"
    bottom = "🩳"
else:
    top = "?"
    middle = "?"
    bottom = "?"
    
from flask import Flask

app = Flask(__name__)

@app.route("/")
def render():
    return "<h1>Emoji Forecast</h1><p>" + top + "</p>" + "<p>" + middle + "</p>" + "<p>" + bottom + "</p>"
