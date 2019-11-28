from flask import Flask, escape, request
import sys
import subprocess
sys.path.append(".")
import scraper

app = Flask(__name__)

@app.route('/')
def welcome():
    name = request.args.get("name", "Welcome to bankier scraping website")
    spider_name = "scraper\\scraper.py"
    subprocess.check_output(['scrapy', 'runspider', spider_name])
    return f'{escape(name)}!'