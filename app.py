from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Steam API Configuration - UPDATE THESE WITH YOUR VALUES
STEAM_API_KEY = "BB2F192F6601D0B7D61EE485B0B5242F"
STEAM_USER_ID = "76561199208258488"

# Sample data for favorites
favorites_data = {
    "games": [
        {"id": 1, "name": "Elden Ring", "rating": 9.5, "category": "games", "details": "Amazing open-world action RPG with incredible boss design and a beautiful, interconnected world. The sense of exploration is unmatched."},
        {"id": 2, "name": "Hollow Knight", "rating": 9, "category": "games", "details": "Metroidvania masterpiece with challenging combat, beautiful hand-drawn art, and deep lore hidden throughout the kingdom."},
        {"id": 3, "name": "The Witcher 3", "rating": 9, "category": "games", "details": "Epic story-driven RPG with complex characters and meaningful side quests. One of the best narratives in gaming."},
    ],
    "movies": [
        {"id": 4, "name": "Inception", "rating": 9.5, "category": "movies", "details": "Mind-bending sci-fi masterpiece with stunning visuals and an intricate plot about shared dreams and consciousness."},
        {"id": 5, "name": "The Matrix", "rating": 9, "category": "movies", "details": "Groundbreaking cyberpunk film with philosophical depth and revolutionary action sequences for its time."},
    ]
}

def get_steam_games():
    """
    Fetch games from Steam Web API
    Returns a list of games with their playtime data
    """
    try:
        # Get owned games
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1"
        params = {
            "key": STEAM_API_KEY,
            "steamid": STEAM_USER_ID,
            "include_appinfo": True,
            "include_played_free_games": True,
            "format": "json"
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "response" not in data or "games" not in data["response"]:
            print("No games found in Steam API response")
            return []
        
        games = data["response"]["games"]
        
        # Transform Steam data to match template format
        transformed_games = []
        for game in games:
            # Calculate hours played
            minutes = game.get("playtime_forever", 0)
            hours = round(minutes / 60, 1)
            
            # Only include games with playtime
            if hours > 0:
                transformed_games.append({
                    "title": game.get("name", "Unknown Game"),
                    "hours": hours,
                    "platform": "Steam",
                    "appid": game.get("appid")
                })
        
        return sorted(transformed_games, key=lambda x: x["hours"], reverse=True)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Steam games: {e}")
        return []

# Games with platform and completion info (fallback data if API fails)
fallback_games = [
    {"title": "Hollow Knight", "completionDate": "2023-06-15", "hours": 45, "platform": "Steam", "completion": 100},
    {"title": "Celeste", "completionDate": "2023-04-22", "hours": 28, "platform": "PlayStation", "completion": 100},
    {"title": "Hades", "completionDate": "2023-08-10", "hours": 52, "platform": "PlayStation", "completion": 100},
    {"title": "Stardew Valley", "completionDate": "2024-02-14", "hours": 180, "platform": "Steam", "completion": 100},
    {"title": "God of War", "completionDate": "2024-01-20", "hours": 35, "platform": "PlayStation", "completion": 85},
    {"title": "Baldur's Gate 3", "completionDate": "2024-03-10", "hours": 120, "platform": "Steam", "completion": 78},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/movies")
def movies():
    return render_template("category.html", category="movies", items=favorites_data["movies"], title="Movies")

@app.route("/favorites")
def favorites():
    return render_template("favorites.html", favorites=favorites_data)

@app.route("/favorites/<int:item_id>")
def favorite_detail(item_id):
    for category in favorites_data.values():
        for item in category:
            if item["id"] == item_id:
                return render_template("favorite_detail.html", item=item)
    return "Not found", 404

@app.route("/games")
def games():
    # Try to fetch from Steam API, fall back to hardcoded data if it fails
    steam_games = get_steam_games()
    games_to_display = steam_games if steam_games else fallback_games
    return render_template("games.html", games=games_to_display)

if __name__ == "__main__":
    app.run(debug=True)