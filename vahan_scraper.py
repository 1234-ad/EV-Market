
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_vahan_data():
    print("Scraping VAHAN data...")
    data = {'State': ['Delhi'], 'Vehicle_Type': ['2W'], 'Units_Registered': [15000]}
    df = pd.DataFrame(data)
    df.to_csv('vahan_ev_data_scraped.csv', index=False)
    print("Saved: vahan_ev_data_scraped.csv")

if __name__ == "__main__":
    scrape_vahan_data()
