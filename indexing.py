import requests
import json

# Service account JSON key file ka path
SERVICE_ACCOUNT_FILE = "indexing-api.json"

# Google Indexing API endpoint
API_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# URLs jo index karne hain
URLS_TO_INDEX = [
    "https://ubg880.github.io/10-minutes-till-dawn.html",
"https://ubg880.github.io/11-11.html",
"https://ubg880.github.io/12-mini-battles-2.html",
"https://ubg880.github.io/12-minibattles.html",
"https://ubg880.github.io/18-wheeler-cargo-simulator.html",
"https://ubg880.github.io/1v1-lol-offline.html",
"https://ubg880.github.io/1v1-lol.html",
"https://ubg880.github.io/2-minute-football.html",
"https://ubg880.github.io/2048-multitask.html",
"https://ubg880.github.io/2048.html",
"https://ubg880.github.io/3d-car-simulator.html",
"https://ubg880.github.io/3d-monster-truck-skyroads.html",
"https://ubg880.github.io/3d-moto-simulator-2.html",
"https://ubg880.github.io/4th-and-goal-2022.html",
"https://ubg880.github.io/4x4-drive-offroad.html",
"https://ubg880.github.io/8-ball-pool.html",
"https://ubg880.github.io/8bit-fiesta.html",
"https://ubg880.github.io/9-balls-pool.html",
"https://ubg880.github.io/a-dance-of-fire-and-ice.html",
"https://ubg880.github.io/a-pretty-odd-bunny-roast-it.html",
"https://ubg880.github.io/a-pretty-odd-bunny.html",
"https://ubg880.github.io/a-small-world-cup.html",
"https://ubg880.github.io/air-hockey-championship-deluxe.html",
"https://ubg880.github.io/aliens-nest.html",
"https://ubg880.github.io/amazing-bubble-breaker.html",
"https://ubg880.github.io/amazing-bubble-connect.html",
"https://ubg880.github.io/among-us.html",
"https://ubg880.github.io/animal-arena.html",
"https://ubg880.github.io/ape-sling.html",
"https://ubg880.github.io/aqua-thrills.html",
"https://ubg880.github.io/archer-master-3d-castle-defense.html",
"https://ubg880.github.io/archery-world-tour.html",
"https://ubg880.github.io/arithmetica.html",
"https://ubg880.github.io/arrow-pathway.html",
"https://ubg880.github.io/athletics-hero.html",
"https://ubg880.github.io/australian-patience.html",
"https://ubg880.github.io/avalanche.html",
"https://ubg880.github.io/b-cubed.html",
"https://ubg880.github.io/bacon-may-die.html",
"https://ubg880.github.io/bad-ice-cream-2.html",
"https://ubg880.github.io/bad-ice-cream-3.html",
"https://ubg880.github.io/barbershop-inc.html",
"https://ubg880.github.io/basket-and-ball.html",
"https://ubg880.github.io/basket-bros.html",
"https://ubg880.github.io/basket-champs.html",
"https://ubg880.github.io/basket-random.html",
"https://ubg880.github.io/basket-swooshes.html",
"https://ubg880.github.io/basketball-frvr.html",
"https://ubg880.github.io/basketball-legends.html",
"https://ubg880.github.io/basketball-stars.html"
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
