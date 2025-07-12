
import requests
import pandas as pd

def scrape_charging_stations():
    print("Scraping Charging Stations data...")
    data = {'Station_ID': [101], 'City': ['Delhi'], 'No_of_Ports': [10]}
    df = pd.DataFrame(data)
    df.to_csv('charging_stations_scraped.csv', index=False)
    print("Saved: charging_stations_scraped.csv")

if __name__ == "__main__":
    scrape_charging_stations()
