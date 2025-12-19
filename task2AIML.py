import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\LENOVO\Downloads\archive\netflix_titles.csv")
# 1. Check missing values formally

print("Missing values in each column:")
print(df.isnull().sum())

#  missing values

df["country"] = df["country"].fillna("Unknown")
df["director"] = df["director"].fillna("No Director Listed")

print("\nMissing values handled for 'country' and 'director'.")

# new columns with NaN
df["duration_minutes"] = np.nan
df["seasons"] = np.nan

#  duration for Movies (in minutes)
df.loc[df["type"] == "Movie", "duration_minutes"] = (
    df.loc[df["type"] == "Movie", "duration"]
    .str.extract(r'(\d+)')
    .astype(float)
)

# number of seasons for TV Shows
df.loc[df["type"] == "TV Show", "seasons"] = (
    df.loc[df["type"] == "TV Show", "duration"]
    .str.extract(r'(\d+)')
    .astype(float)
)

print("\nDuration features created: 'duration_minutes' and 'seasons'.")

# binary feature

df["Is_Recent"] = np.where(df["release_year"] >= 2015, 1, 0)

print("\nBinary feature 'Is_Recent' created.")

# preview

print(df.head())
