from flask import Flask, render_template, request
import requests
from datetime import datetime
import os
from pathlib import Path

app = Flask(__name__)

def load_env_file():
    env_path = Path(__file__).with_name(".env")

    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env_file()

# Steam API Configuration - set in .env or environment variables
STEAM_API_KEY = os.environ.get("STEAM_API_KEY", "")
STEAM_USER_ID = os.environ.get("STEAM_USER_ID", "")
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "")
GITHUB_URL = os.environ.get("GITHUB_URL", "")
LINKEDIN_URL = os.environ.get("LINKEDIN_URL", "")
RESUME_URL = os.environ.get("RESUME_URL", "")

# Sample data for featured items
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

def get_game_achievements(appid):
    """
    Fetch achievements for a specific game
    Returns dict with unlocked count, total count, and percentage
    """
    try:
        url = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1"
        params = {
            "key": STEAM_API_KEY,
            "steamid": STEAM_USER_ID,
            "appid": appid,
            "format": "json"
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if "playerstats" not in data or "achievements" not in data["playerstats"]:
            print(f"No achievements found for app {appid}")
            return None
        
        achievements = data["playerstats"]["achievements"]
        unlocked = sum(1 for ach in achievements if ach.get("achieved", 0) == 1)
        total = len(achievements)
        
        if total == 0:
            return None
        
        completion = round((unlocked / total) * 100, 1)
        print(f"Found {unlocked}/{total} achievements for app {appid}")
        
        return {
            "unlocked": unlocked,
            "total": total,
            "completion": completion
        }
    
    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching achievements for app {appid}: {e}")
        return None

def get_steam_games():
    """
    Fetch games from Steam Web API
    Returns a list of games with their playtime and achievement data
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
                appid = game.get("appid")
                game_data = {
                    "title": game.get("name", "Unknown Game"),
                    "hours": hours,
                    "platform": "Steam",
                    "appid": appid
                }
                
                # Fetch achievements if available
                achievements = get_game_achievements(appid)
                if achievements:
                    game_data["achievements_unlocked"] = achievements["unlocked"]
                    game_data["achievements_total"] = achievements["total"]
                    game_data["achievements_completion"] = achievements["completion"]
                
                transformed_games.append(game_data)
        
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

featured_projects = [
    {
        "title": "ASL Dictionary Website",
        "summary": "A website built with Svelte, TypeScript, HTML, and JavaScript to help people learn ASL. It won first place at the 2024 Kent State Hackathon.",
        "stack": ["Svelte", "TypeScript", "HTML", "JavaScript"],
        "links": [
            {"label": "GitHub", "url": "https://github.com/ManOfNeptune27/asl-dictionary"}
        ]
    },
    {
        "title": "ASL Department Dictionary",
        "summary": "A school project for organizing and storing teachers' ASL vocabulary in one consolidated dictionary for day-to-day use.",
        "stack": ["Web App", "Dictionary"],
        "links": [
            {"label": "GitHub", "url": "https://github.com/ManOfNeptune27/ASLDepartmentDictionary"}
        ]
    },
    {
        "title": "The Cattery",
        "summary": "A Unity game made by Team A about creating cats by baking them from dough.",
        "stack": ["C#"],
        "links": [
            {"label": "GitHub", "url": "https://github.com/knotpil/GDP-TeamA"}
        ]
    }
]

skill_groups = [
    {
        "title": "Languages",
        "items": ["Python", "JavaScript", "HTML", "CSS"]
    },
    {
        "title": "Frameworks",
        "items": ["Flask", "Jinja2", "APIs", "Responsive UI"]
    },
    {
        "title": "Interests",
        "items": ["Game Dev", "Accessibility", "ASL", "Web Design"]
    }
]

contact_links = [
    {"label": "GitHub", "url": GITHUB_URL},
    {"label": "LinkedIn", "url": LINKEDIN_URL},
    {"label": "Resume", "url": RESUME_URL},
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        featured_projects=featured_projects,
        skill_groups=skill_groups,
        contact_links=contact_links,
        contact_email=CONTACT_EMAIL,
    )


@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        featured_projects=featured_projects,
        title="Projects",
    )


@app.route("/skills")
def skills():
    return render_template(
        "skills.html",
        skill_groups=skill_groups,
        title="Skills",
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        contact_links=contact_links,
        contact_email=CONTACT_EMAIL,
        title="Contact",
    )

@app.route("/movies")
def movies():
    return render_template("category.html", category="movies", items=favorites_data["movies"], title="Movies")

@app.route("/games")
def games():
    # Try to fetch from Steam API, fall back to hardcoded data if it fails
    steam_games = get_steam_games()
    games_to_display = steam_games if steam_games else fallback_games
    return render_template("games.html", games=games_to_display)

if __name__ == "__main__":
    app.run(debug=True)