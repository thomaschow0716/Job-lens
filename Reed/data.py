import os

from dotenv import load_dotenv

from requests.auth import HTTPBasicAuth
import requests

load_dotenv()
api_key = os.getenv('API_KEY')

url = "https://www.reed.co.uk/api/1.0/search?keywords=accountant&location=Londonn&distancefromlocation=15"
headers = {'Accept': 'application/json'}
auth = HTTPBasicAuth(api_key, '')

req = requests.get(url, headers = headers, auth = auth)
print(req.status_code)
print(req.text)