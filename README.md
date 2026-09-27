# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-TF--IDF-orange?style=for-the-badge&logo=scikit-learn)
![NLP](https://img.shields.io/badge/NLP-Cosine%20Similarity-blueviolet?style=for-the-badge)
![OMDb](https://img.shields.io/badge/OMDb-API-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

A **content-based movie recommendation system** that recommends similar movies based on genres, keywords, cast, director, and movie overview.

The recommendation engine uses **TF-IDF Vectorization** and **Cosine Similarity**, while a **Flask web application** provides an interactive interface with movie posters and IMDb ratings fetched through the OMDb API.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Web Application](#web-application)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Tech Stack](#tech-stack)
- [Key Concepts](#key-concepts)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

<a id="about-the-project"></a>
# 🔍 About the Project

This project implements a **content-based movie recommendation system** that recommends movies similar to a movie selected by the user.

Instead of relying on user ratings or collaborative filtering, the system analyzes the **content and metadata of movies**.

The following information is combined into a single feature representation:

- 🎭 Genres
- 🔑 Keywords
- 🌟 Top 3 Cast Members
- 🎬 Director
- 📝 Movie Overview

The processed movie information is transformed into numerical vectors using **TF-IDF**, and **Cosine Similarity** is used to identify movies with similar content.

The recommendation artifacts are precomputed during model development and serialized using Pickle for efficient reuse in the Flask application.

---

<a id="features"></a>
# ✨ Features

## 🤖 Recommendation Engine

- Content-based movie recommendation
- TF-IDF based feature representation
- Cosine similarity for movie matching
- Top **5 similar movies** generated for each query
- Precomputed similarity matrix for faster recommendations

## 🌐 Web Application

- Flask backend
- Jinja2 templating
- Responsive HTML/CSS frontend
- Minimal dark glassmorphism interface
- Movie selection dropdown
- One-click recommendation generation
- Responsive movie card layout

## 🎬 Movie Information

- Movie posters fetched from the **OMDb API**
- IMDb ratings displayed for recommended movies
- Local fallback poster when movie artwork is unavailable

## ⚡ Performance

- Precomputed similarity matrix
- Serialized recommendation data
- OMDb API responses cached during application runtime
- No model training required when running the Flask application

---

<a id="how-it-works"></a>
# 🧠 How It Works

## Step 1 — Feature Extraction

Relevant movie information is combined into a single `tags` feature.

```text
tags =
overview
+ genres
+ keywords
+ top 3 cast
+ director
```

For example:

```text
Avatar

overview:
A paraplegic marine dispatched to the moon Pandora...

genres:
Action Adventure Fantasy Science Fiction

keywords:
culture clash, future, space war

cast:
Sam Worthington Zoe Saldana Sigourney Weaver

director:
James Cameron
```

---

## Step 2 — Text Preprocessing

The original TMDB dataset contains several columns stored as JSON-like strings.

These columns are parsed and transformed into usable Python structures.

The preprocessing pipeline extracts:

* Movie genres
* Relevant keywords
* Top 3 cast members
* Director

Names are normalized by removing spaces to improve matching during vectorization.

```text
Sam Worthington
        ↓
SamWorthington
```

---

## Step 3 — TF-IDF Vectorization

The combined `tags` feature is converted into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF assigns greater importance to terms that are more distinctive while reducing the importance of common words.

The vectorizer used during model development:

```python
TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)
```

The resulting vectors represent each movie as a numerical feature vector.

---

## Step 4 — Cosine Similarity

After vectorization, **Cosine Similarity** is used to measure the similarity between movies.

```text
Similarity Score → 1.0
        ↓
Highly Similar

Similarity Score → 0.0
        ↓
Less Similar
```

The similarity scores are stored in a precomputed similarity matrix.

For approximately 4,800 movies:

```text
Similarity Matrix
≈ 4800 × 4800
```

This allows the Flask application to retrieve recommendations without recalculating similarity for every request.

---

## Step 5 — Generate Recommendations

When a user selects a movie, the application:

```text
Selected Movie
      ↓
Find Movie Index
      ↓
Retrieve Similarity Scores
      ↓
Sort Movies by Similarity
      ↓
Remove Selected Movie
      ↓
Select Top 5 Movies
      ↓
Fetch Poster + IMDb Rating
      ↓
Display Recommendations
```

Each recommendation displays:

* 🎬 Movie title
* 🖼️ Movie poster
* ⭐ IMDb rating

---

<a id="dataset"></a>
# 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**.

## Dataset Files

| File                    | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `tmdb_5000_movies.csv`  | Movie information including title, overview, genres and keywords |
| `tmdb_5000_credits.csv` | Cast and crew information                                        |

## Dataset Overview

| Feature             | Details                                    |
| -------------------- | -------------------------------------------- |
| Dataset              | TMDB 5000 Movies Dataset                     |
| Movies               | ~4,800 after preprocessing                   |
| Main Features        | Overview, genres, keywords, cast, director   |
| Recommendation Type  | Content-Based Filtering                      |
| Recommendations      | Top 5 similar movies                         |

---

<a id="project-workflow"></a>
# 🔄 Project Workflow

```text
TMDB Movies Dataset
        +
TMDB Credits Dataset
        ↓
    Data Merging
        ↓
 Feature Selection
        ↓
 Data Preprocessing
        ↓
 ┌──────────────────────┐
 │ Extract Genres       │
 │ Extract Keywords     │
 │ Extract Top 3 Cast   │
 │ Extract Director     │
 └──────────────────────┘
        ↓
    Tag Creation
        ↓
 TF-IDF Vectorization
        ↓
 Cosine Similarity
        ↓
 Save Processed Data
        ↓
 ┌──────────────────────┐
 │    Flask Backend     │
 └──────────────────────┘
        ↓
 User Selects Movie
        ↓
 Generate Top 5 Movies
        ↓
 ┌──────────────────────┐
 │       OMDb API       │
 │ Posters + IMDb Rate  │
 └──────────────────────┘
        ↓
    Web Interface
```

---

<a id="web-application"></a>
# 🌐 Web Application

The recommendation engine is integrated into a Flask-based web application.

The frontend uses a **minimal dark glassmorphism design** with a cinematic visual style.

## User Flow

```text
Select a Movie
      ↓
Click "Recommend"
      ↓
Recommendation Engine
      ↓
Top 5 Similar Movies
      ↓
Posters + IMDb Ratings
```

## Interface Features

* 🎬 Movie selection dropdown
* 🔍 Recommendation button
* 🖼️ Movie poster cards
* ⭐ IMDb ratings
* 🌑 Dark cinematic UI
* 🪟 Glassmorphism cards
* ✨ Reflective/shader-style ambient background
* 📱 Responsive layout

---

<a id="project-structure"></a>
# 📁 Project Structure

```text
movies-recommendation-system/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── poster-placeholder.svg
```

## File Description

| File                             | Purpose                                    |
| --------------------------------- | -------------------------------------------- |
| `app.py`                          | Flask application and recommendation logic  |
| `movie_dict.pkl`                  | Processed movie data                         |
| `similarity.pkl`                  | Precomputed cosine similarity matrix         |
| `templates/index.html`            | Jinja2 frontend template                     |
| `static/style.css`                | UI styling and responsive design             |
| `static/poster-placeholder.svg`   | Fallback poster                              |
| `requirements.txt`                | Python dependencies                          |

---

<a id="installation"></a>
# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/movies-recommendation-system.git

cd movies-recommendation-system
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Main dependencies include:

```text
Flask
Pandas
Requests
Scikit-learn
```

---

<a id="configuration"></a>
# 🔐 Configuration

The application uses the **OMDb API** to retrieve:

* Movie posters
* IMDb ratings

Set your OMDb API key as an environment variable.

### Windows PowerShell

```powershell
$env:OMDB_API_KEY="YOUR_OMDB_API_KEY"
```

### Windows CMD

```cmd
set OMDB_API_KEY=YOUR_OMDB_API_KEY
```

### macOS / Linux

```bash
export OMDB_API_KEY="YOUR_OMDB_API_KEY"
```

> **Never commit your API key directly to GitHub.**

---

<a id="running-the-application"></a>
# ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Select a movie from the dropdown and click:

```text
🔍 Recommend
```

The application will generate the **top 5 similar movies** and display their posters and IMDb ratings.

---

<a id="tech-stack"></a>
# 🛠️ Tech Stack

| Technology           | Purpose                          |
| ---------------------- | ----------------------------------- |
| **Python**             | Core programming language           |
| **Pandas**             | Data manipulation                   |
| **NumPy**              | Numerical operations                |
| **Scikit-learn**       | TF-IDF and cosine similarity        |
| **Flask**              | Backend web framework               |
| **Jinja2**             | Dynamic HTML rendering              |
| **HTML5**              | Frontend structure                   |
| **CSS3**               | UI styling and responsive layout    |
| **OMDb API**           | Posters and IMDb ratings            |
| **Pickle**             | Serialization of processed data     |
| **Jupyter Notebook**   | Model development                   |

---

<a id="key-concepts"></a>
# 💡 Key Concepts

| Concept                     | Explanation                                                          |
| ----------------------------- | ------------------------------------------------------------------------ |
| **Content-Based Filtering**  | Recommends movies based on similarity between their content features   |
| **TF-IDF**                   | Converts textual movie information into numerical vectors              |
| **Cosine Similarity**        | Measures similarity between movie feature vectors                      |
| **Feature Engineering**      | Combines multiple movie attributes into a single `tags` feature        |
| **NLP**                      | Used to process and represent movie-related text                       |
| **Model Serialization**      | Stores processed data and similarity results for reuse                 |
| **Flask**                    | Serves the recommendation system through a web interface               |
| **API Integration**          | Retrieves additional movie metadata from OMDb                          |

---

<a id="future-improvements"></a>
# 🔮 Future Improvements

Potential improvements include:

* [ ] Movie search with autocomplete
* [ ] Genre-based filtering
* [ ] Display release year and movie overview
* [ ] Movie trailer integration
* [ ] Recommendation explanations
* [ ] User recommendation history
* [ ] Collaborative filtering
* [ ] Hybrid recommendation system
* [ ] User-specific recommendations
* [ ] Cloud deployment
* [ ] Improved API fallback handling

---

<a id="author"></a>
# 👤 Author

**Momin Saad Asrar**

**B.E. CSE (AI-ML)**
Anjuman-I-Islam's Kalsekar Technical Campus

📧 **Email:** [saadizhan123@gmail.com](mailto:saadizhan123@gmail.com)

🔗 **LinkedIn:**
[https://www.linkedin.com/in/saad-momin-9a88542bb](https://www.linkedin.com/in/saad-momin-9a88542bb)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.
