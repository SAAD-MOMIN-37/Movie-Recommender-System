# 🎬 Movies Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-TF--IDF-orange?style=for-the-badge&logo=scikit-learn)
![NLP](https://img.shields.io/badge/NLP-Cosine%20Similarity-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

A content-based movie recommendation system that suggests similar movies based on genres, keywords, cast, director, and overview using **TF-IDF Vectorization** and **Cosine Similarity**. Built on the TMDB 5000 Movies Dataset.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Project Workflow](#project-workflow)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)

---

## 🔍 About the Project

Ever wondered how Netflix or YouTube suggests "similar" content? This project builds exactly that — a **content-based filtering** recommendation system for movies.

Given a movie title, the system finds the **top 10 most similar movies** by analyzing:
- 🎭 Genres
- 🔑 Keywords
- 🎬 Director
- 🌟 Top 3 Cast Members
- 📝 Plot Overview

Key highlights:
- **TMDB 5000** movies in the database
- **TF-IDF Vectorizer** with 5000 features
- **Cosine Similarity** matrix for fast lookups
- Search, browse, batch recommend — full interactive system
- Model saved with **Pickle** for instant reuse

---

## 📊 Dataset

**TMDB 5000 Movies Dataset**

| File | Details |
|---|---|
| `tmdb_5000_movies.csv` | Movie info — title, overview, genres, keywords |
| `tmdb_5000_credits.csv` | Cast and crew information |

| Feature | Details |
|---|---|
| Total Movies | ~4800 (after cleaning) |
| Key Columns Used | title, overview, genres, keywords, cast, crew |
| Target | Find top 10 similar movies |

---

## 🧠 How It Works

### Step 1 — Feature Extraction
All relevant info is combined into one **"tags"** column:

```
tags = overview + genres + keywords + top 3 cast + director
```

Example for **Avatar**:
```
tags = "a paraplegic marine dispatched to the moon pandora... 
        action adventure fantasy sciencefiction 
        cultureclash future space war 
        SamWorthington ZoeSaldana SigourneyWeaver 
        JamesCameron"
```

### Step 2 — TF-IDF Vectorization
Each movie's tags are converted into a **numeric vector** of 5000 features.

> **TF-IDF** (Term Frequency-Inverse Document Frequency) gives higher weight to words that are unique to a movie and lower weight to common words like "the", "a", "is".

### Step 3 — Cosine Similarity
The **similarity score** between every pair of movies is calculated.

```
Similarity Score = cos(angle between two vectors)
Score = 1.0  →  Identical movies
Score = 0.0  →  Completely different movies
```

### Step 4 — Recommendation
For a given movie, find the **top 10 movies** with the highest similarity scores.

---

## 🔄 Project Workflow

```
1. Data Loading
   - tmdb_5000_movies.csv + tmdb_5000_credits.csv
   - Merge on 'title'
        ↓
2. Feature Selection
   - Keep: movie_id, title, overview, genres, keywords, cast, crew
        ↓
3. Data Preprocessing
   - Parse JSON columns using ast.literal_eval()
   - Extract top 3 cast members
   - Extract director from crew
   - Remove spaces (e.g. "Sam Worthington" → "SamWorthington")
        ↓
4. Tag Creation
   - tags = overview + genres + keywords + cast + director
        ↓
5. TF-IDF Vectorization
   - max_features = 5000
   - stop_words = 'english'
        ↓
6. Cosine Similarity Matrix
   - Shape: (4800, 4800)
        ↓
7. Recommendation Function
   - Input: movie title
   - Output: top 10 similar movies
        ↓
8. Save Models
   - movies.pkl (dataframe)
   - similarity.pkl (similarity matrix)
```

---

## 🎯 Example Output

```python
recommend('Avatar')

# Output:
Top 10 recommendations for 'Avatar':
1. Guardians of the Galaxy
2. Aliens
3. Star Wars: Clone Wars
4. Star Trek Into Darkness
5. Star Trek Beyond
6. Alien: Resurrection
7. Alien
8. Lockout
9. Jason X
10. The Martian
```

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/movies-recommendation-system.git
cd movies-recommendation-system
```

### 2. Install Dependencies
```bash
pip install numpy pandas scikit-learn pickle5
```

### 3. Run Training Notebook
```bash
jupyter notebook PRJ_Movies_Recommendation_System_Training.ipynb
```

### 4. Run Testing / Recommendations
```bash
jupyter notebook PRJ_Movies_Recommendation_System_Testing.ipynb
```

### 5. Get Recommendations (Inside Testing Notebook)
```python
# Get top 10 recommendations
recommend('The Dark Knight')

# Search movies by keyword
search_movies('Batman')

# Batch recommendations for multiple movies
batch_recommend(['Inception', 'Titanic', 'Avatar'])
```

---

## 📁 Project Structure

```
movies-recommendation-system/
│
├── tmdb_5000_movies.csv                          # Movies dataset
├── tmdb_5000_credits.csv                         # Credits dataset
│
├── PRJ_Movies_Recommendation_System_Training.ipynb  # Training notebook
├── PRJ_Movies_Recommendation_System_Testing.ipynb   # Testing notebook
│
├── models/
│   ├── movies.pkl                                # Processed movies dataframe
│   └── similarity.pkl                            # Cosine similarity matrix
│
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas / NumPy | Data manipulation |
| ast | Parsing JSON-like columns |
| Scikit-learn (TF-IDF) | Text vectorization |
| Scikit-learn (Cosine Similarity) | Similarity computation |
| Pickle | Model serialization |
| Jupyter Notebook | Development environment |

---

## 💡 Key Concepts Used

| Concept | Explanation |
|---|---|
| **Content-Based Filtering** | Recommends movies similar to the one you liked, based on movie features |
| **TF-IDF** | Converts text to numbers — rare/unique words get higher importance |
| **Cosine Similarity** | Measures angle between two vectors — closer to 1 means more similar |
| **Feature Engineering** | Combined multiple columns (genres, cast, etc.) into one powerful 'tags' feature |
| **ast.literal_eval** | Converts string representation of JSON lists into actual Python lists |

---

## 👤 Author

**Momin Saad Asrar**  
B.E. CSE (AI-ML) — Anjuman-I-Islam's Kalsekar Technical Campus  
📧 saadizhan123@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN)

---

> ⭐ If you found this project helpful, please give it a star!
