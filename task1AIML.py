
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1.  Netflix dataset

df = pd.read_csv(r"C:\Users\LENOVO\Downloads\archive\netflix_titles.csv")

# 2. first 10 rows

print("First 10 rows ")
print(df.head(10))


# 3. Dataset shape 

print("\nDataset Shape")
print(df.shape)


# 4. Dataset info

print("\nDataset Info")
print(df.info())


# 5. Statistical summary (including categorical data)

print("\nStatistical Summary:")
print(df.describe(include='all'))


# 6. duplicate show_id values

duplicate_count = df.duplicated(subset='show_id').sum()
print(f"\nNumber of duplicate show_id entries: {duplicate_count}")

# Drop duplicate show_id 
df.drop_duplicates(subset='show_id', inplace=True)

# 7. Drop the 'description' column

df.drop(columns=['description'], inplace=True)

print("\n'description' column dropped successfully.")

