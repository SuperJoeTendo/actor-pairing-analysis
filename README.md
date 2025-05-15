# 🎬 Actor Clustering for Smarter Casting Decisions

## ❓ Question
Who should be cast for a certain genre to create good chemistry among actors?  
Which actors are most frequently cast in higher-rated movies?

---

## 📌 Module Post Extension
We extended Grace’s Modules 2 and 3 Medium assignments. We continued using the IMDb dataset and kept **casting directors** as our stakeholder.

---

## 👤 Stakeholder: Casting Directors
It is often difficult to determine which actors will have good enough chemistry to be a strong on-screen pairing — especially if they’ve never acted together before. This project uses **data analysis** to help casting directors predict good actor pairings and reduce time spent on chemistry tests and casting misfires.

---

## 🎓 Subject Matter Expertise
We considered:
- Actor collaboration patterns
- Activity spans across different years
- Gaps in acting careers (hiatuses)
- How casting directors make chemistry-based casting choices based on past experience

---

## 🎯 Decision
**Help casting directors decide which actors to cast in a movie** based on performance traits, compatibility, and career characteristics.

---

## 📂 Data Used
- **IMDb Dataset** (`.json`) — includes tens of thousands of movies and actor information
- **TMDB 5000 Movie Dataset** (from Kaggle) — includes 5,000 movies with popularity and revenue info

---

## 🧹 Cleaned Data
We pulled:
- Average movie rating
- Number of movies per actor
- Total years active
- Actor popularity
- Total gross revenue

We filtered out actors with fewer than 3 movies to focus on more established talent. Only the top 5 actors per cluster were shown to keep results clear and digestible.

---

## 🔁 How We Extended the Module Posts
We combined Grace’s Module 2 and 3 posts:
- **Module 2**: Focused on closeness centrality to determine which actors might work well together in a **drama** movie.
- **Module 3**: Focused on cosine similarity and degree centrality to decide which actors should be cast for specific **genres**.

Our extension added:
- A **new dataset** (TMDB)
- New features: **popularity** and **gross revenue**
- A **clustering method** to group actors by similarity and performance traits

---

## 🧪 Methods from the Course: Clustering
We used the **KMeans clustering algorithm** to group actors into types based on:
- `avg_rating`
- `movie_count`
- `avg_popularity`
- `total_revenue`

---

## 📊 Cluster Insights
Each cluster revealed a unique actor group:

1. **Steady Performers**  
   Moderate movie count, solid ratings, consistent presence.

2. **Upcoming Performers**  
   Fewer movies, lower ratings, still developing — but show potential.

3. **Veterans**  
   Long careers, high ratings, dependable and widely experienced.

4. **Critically Strong**  
   Fewer movies but high ratings — ideal for drama or award-contending roles.

These clusters allow casting directors to pair actors who **complement each other** based on data — not just reputation.

---

## 📈 Visualizations
- 📊 **Violin plots** show how each feature differs across clusters.
- 📄 A final CSV includes all actors with their cluster labels for further exploration.

---

## 📁 Files Included
- `imdb_movies_2000to2022.prolific.json`
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`
- `actor_clusters.csv` (final cleaned and labeled dataset)

---

## 🛠 Tools Used
- Python (Google Colab)
- pandas
- scikit-learn (KMeans, StandardScaler)
- seaborn & matplotlib (for visualization)

---

## 👥 Authors
- Grace Yu  
- Joseph Benson

---
