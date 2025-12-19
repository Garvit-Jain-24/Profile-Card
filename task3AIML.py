import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\LENOVO\Downloads\archive\netflix_titles.csv")

# 1. Bar Chart

type_counts = df['type'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values)
plt.title("Distribution of Content on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()

# 2. Histogram: Release Year Distribution

plt.figure(figsize=(8,5))
plt.hist(df['release_year'], bins=30)
plt.title(" Release Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()


# 3. Bar Chart: Top 10 Countries by Content Count

top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.barh(top_countries.index, top_countries.values)
plt.title("Top 10 Countries by Number of Netflix Releases")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()


# 4. Boxplot: Movie Duration vs Is_Recent
recent_movies = df[df['type'] == 'Movie']

data = [
    recent_movies[recent_movies["Is_Recent"] == 0]["duration_minutes"].dropna(),
    recent_movies[recent_movies["Is_Recent"] == 1]["duration_minutes"].dropna()
]

plt.figure(figsize=(6,4))
plt.boxplot(data, labels=['Older Movies', 'Recent Movies'])
plt.title("Movie Duration Comparison: Recent vs Older Movies")
plt.ylabel("Duration (Minutes)")
plt.show()


# 5. Genre Frequency 

genres = df["listed_in"].dropna().str.split(', ')
genre_counts = pd.Series([g for sublist in genres for g in sublist]).value_counts().head(1)

