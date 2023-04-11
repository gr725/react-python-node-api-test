from flask import Flask,jsonify,request
from flask_cors import CORS

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/merchant_page_initial_data/<string:path>')
def get_info(path):
    title = request.args.get('title')
    description = request.args.get('description')
        # siteUrl = request.args.get('siteUrl')

    # # Lets Get Meta Data
    influencer_description    = description;
    influencer_banner         = "https://banner_img";
    
    data = {
        "title" : title,
        "description" : influencer_description,
        "banner" : influencer_banner,
    }

    return jsonify(data)

@app.route('/api/get_meta_data')
def get_meta_data():
    siteUrl = request.args.get('siteUrl')

    # Lets Get Meta Data
    influencer_description    = "";
    influencer_banner         = "";
    
    # Base URL - To Fetch Data
    # siteUrl             = "https://github.com/"

    # Lets Get Data & Store it in Object
    html_content        = requests.get(siteUrl).text
   
    # Parse HTML Code With Beautiful Soup
    soup                = BeautifulSoup(html_content, "html.parser") 

    # Lets Get Title Data
    title          = soup.title.string

    # Search in Meta
    for meta in soup.findAll("meta"):
        meta_name = meta.get('name', '').lower()
        meta_property = meta.get('property', '').lower()
        
        # If Data found assign it
        if meta_name == 'og:description' or meta_property == "og:description":
            influencer_description = meta['content']

        if meta_name == 'og:image' or meta_property == "og:image":
            influencer_banner = meta['content']
                        
    data = {
        "title" : title,
        "description" : influencer_description,
        "banner" : influencer_banner,
    }

    return jsonify(data)
  
