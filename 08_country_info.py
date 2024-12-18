import requests

BASE_URL = "https://restcountries.com/v3.1/name/"

# Fetch country details
def fetch_country_info(country):
    response = requests.get(BASE_URL + country)

    if response.status_code == 200:
        data = response.json()[0]
        print(f"Country: {data['name']['common']}")
        print(f"Capital: {data['capital'][0]}")
        print(f"Population: {data['population']}")
        print(f"Region: {data['region']}")
    else:
        print("Country not found!")

country_name = input("Enter a country name: ").lower()
fetch_country_info(country_name)