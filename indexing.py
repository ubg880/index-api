import requests
import json

# Service account JSON key file ka path
SERVICE_ACCOUNT_FILE = "indexing-api.json"

# Google Indexing API endpoint
API_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# URLs jo index karne hain
URLS_TO_INDEX = [
    "https://example.com/live-streaming-page",
    "https://example.com/game-page"
]

# Function to get Access Token
def get_access_token():
    from google.oauth2 import service_account
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/indexing"]
    )
    return credentials.token

# Function to send Indexing request
def index_url(url):
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }
    data = {"url": url, "type": "URL_UPDATED"}
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    return response.json()

# Run indexing for all URLs
for url in URLS_TO_INDEX:
    result = index_url(url)
    print(f"Indexed {url}: {result}")
