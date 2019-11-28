from flask import Flask, escape, request
import sys
sys.path.append(".")
import scraper

app = Flask(__name__)

@app.route('/')
def welcome():
    name = request.args.get("name", "Welcome to bankier scraping website")
    scraper_obj = Scraper()
    scraper_obj.parse()
    return f'{escape(name)}!'