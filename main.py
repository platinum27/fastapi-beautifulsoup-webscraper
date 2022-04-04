from Scrape import Scrape
from requests import HTTPError, TooManyRedirects
from fastapi import FastAPI, Query, HTTPException

import json

app = FastAPI()

@app.get("/")
def root():
    return "The web server is running!"

@app.get("/lmeprices")
def get_lme_prices():
    s = Scrape('s','e')
    return s.summary()