from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)

def getApiKey():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def weatherResult(cityName, apiKey):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=" + apiKey
    re = requests.get(api_url)
    return re.json()
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    error = 0
    cityName = request.form.get("cityName")
    if cityName:
        key = getApiKey()
        data = weatherResult(cityName, key)
    else:
        error = 1
    return render_template('results.html', data=data, cityName=cityName, error=error)


if __name__ == '__main__':
    app.run(debug=True)
