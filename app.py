from flask import Flask, render_template, request

app = Flask(__name__)

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
    ],
    "food": [
        {"id": 6, "name": "Spicy Ramen", "rating": 8.5, "category": "food", "details": "Rich tonkotsu broth with perfectly cooked noodles, topped with soft-boiled egg and green onions. The heat level is just right."},
        {"id": 7, "name": "Sushi Roll Platter", "rating": 9, "category": "food", "details": "Fresh fish, perfectly seasoned rice, and crisp nori. The variety and quality of ingredients makes each bite special."},
    ]
}

# Games with platform and completion info
all_games = [
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

@app.route("/food")
def food():
    return render_template("category.html", category="food", items=favorites_data["food"], title="Food")

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
    return render_template("games.html", games=all_games)

if __name__ == "__main__":
    app.run(debug=True)