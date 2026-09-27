import os
import pickle
from functools import lru_cache
from urllib.parse import quote

import pandas as pd
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MOVIE_FILE = os.path.join(BASE_DIR, "movie_dict.pkl")
SIMILARITY_FILE = os.path.join(BASE_DIR, "similarity.pkl")

# ---------------------------------------------------------
# Load recommendation model
# ---------------------------------------------------------
with open(MOVIE_FILE, "rb") as file:
    movies = pickle.load(file)

with open(SIMILARITY_FILE, "rb") as file:
    similarity = pickle.load(file)

if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

movies = movies.reset_index(drop=True)

movie_list = movies["title"].dropna().unique().tolist()

# ---------------------------------------------------------
# OMDb poster API
# Set your API key as an environment variable:
# Windows PowerShell:
#   $env:OMDB_API_KEY="your_key"
# Linux/macOS:
#   export OMDB_API_KEY="your_key"
# ---------------------------------------------------------
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "8ce18774")

PLACEHOLDER_POSTER = (
    "https://via.placeholder.com/300x450/"
    "171a21/ffffff?text=No+Poster"
)


@lru_cache(maxsize=512)
@lru_cache(maxsize=512)
def fetch_movie_details(movie_title):
    """Fetch poster and IMDb rating from OMDb."""

    if not OMDB_API_KEY:
        return {
            "poster": PLACEHOLDER_POSTER,
            "rating": "N/A"
        }

    try:
        url = (
            "https://www.omdbapi.com/"
            f"?t={quote(movie_title)}"
            f"&apikey={OMDB_API_KEY}"
        )

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("Response") == "True":

            poster = data.get("Poster")

            if not poster or poster == "N/A":
                poster = PLACEHOLDER_POSTER

            rating = data.get("imdbRating")

            if not rating or rating == "N/A":
                rating = "N/A"

            return {
                "poster": poster,
                "rating": rating
            }

    except requests.RequestException:
        pass

    return {
        "poster": PLACEHOLDER_POSTER,
        "rating": "N/A"
    }


def recommend(movie_title):
    """Return the top 5 movies similar to the selected movie."""

    matching_movies = movies[movies["title"] == movie_title]

    if matching_movies.empty:
        return []

    movie_index = matching_movies.index[0]

    distances = similarity[movie_index]

    movie_indices = sorted(
        enumerate(distances),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for index, score in movie_indices:

        title = movies.iloc[index]["title"]

        details = fetch_movie_details(title)

        recommendations.append({
            "title": title,
            "poster": details["poster"],
            "rating": details["rating"]
        })

    return recommendations


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    selected_movie = ""

    if request.method == "POST":
        selected_movie = request.form.get("movie", "").strip()

        if selected_movie:
            recommendations = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


if __name__ == "__main__":
    app.run(debug=True)
