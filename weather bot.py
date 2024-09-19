import requests

API_KEY = '48353c24a8070639992d5177111c1cb1'  # Your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    print(response.url)  # Print URL for debugging
    data = response.json()
    print(data)  # Print response data for debugging
    
    if data.get('cod') == 200:
        main = data['main']
        weather = data['weather'][0]
        city_name = data['name']
        description = weather['description']
        temperature = main['temp']
        humidity = main['humidity']
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error: {data.get('message', 'City not found.')}")
    
def main():
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        get_weather(city)

if __name__ == "__main__":
    main()
