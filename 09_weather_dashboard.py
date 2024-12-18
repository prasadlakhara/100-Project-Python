import requests

# API Configurations
WEATHER_API_KEY = "e4f39c784b3d4331b94d5e77e8123c4b"  # OpenWeatherMap API key
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITIES_API_URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

# API headers for GeoDB Cities API
HEADERS = {
    "X-RapidAPI-Key": "ea2bc1d1d8msh30a48bdb0546ffep1c24fajsndcddbc34c1ab",  # Replace with your RapidAPI key
    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

def get_weather(city):
    """
    Fetch weather details for a given city using OpenWeatherMap API.
    """
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
    response = requests.get(WEATHER_BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}:")
        print(f"- Description: {data['weather'][0]['description'].capitalize()}")
        print(f"- Temperature: {data['main']['temp']}°C")
        print(f"- Humidity: {data['main']['humidity']}%")
        print(f"- Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error fetching weather! Status Code: {response.status_code}")
        print(f"Response: {response.text}")

def get_city_suggestions(query):
    """
    Fetch city suggestions based on the query using GeoDB Cities API.
    """
    params = {"namePrefix": query, "limit": 5}
    response = requests.get(CITIES_API_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and data["data"]:
            cities = [city["name"] for city in data["data"]]
            return cities
        else:
            print("No cities found for the given query.")
            return []
    else:
        print(f"Error fetching city suggestions. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return []

def main():
    """
    Main program to fetch city suggestions and weather details.
    """
    city_query = input("Start typing a city name: ")
    if not city_query.strip():
        print("City query cannot be empty!")
        return

    suggestions = get_city_suggestions(city_query)

    if suggestions:
        print("\nSuggestions:", ", ".join(suggestions))
        selected_city = input("Enter the city name from suggestions: ").strip()
        if selected_city:
            get_weather(selected_city)
        else:
            print("You must enter a valid city name!")
    else:
        print("No suggestions found.")

if __name__ == "__main__":
    main()
