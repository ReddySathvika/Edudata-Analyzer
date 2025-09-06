import numpy as np
import pandas as pd

# -------------------------------
# Step 1: Generate random data with NumPy
# -------------------------------
np.random.seed(42)  # for reproducibility
scores = np.random.randint(50, 100, size=(5, 3))  # 5 students, 3 subjects

print("NumPy Scores Array:\n", scores)

# -------------------------------
# Step 2: Create a Pandas DataFrame
# -------------------------------
df = pd.DataFrame(
    scores,
    columns=["Math", "Science", "English"],
    index=["Student1", "Student2", "Student3", "Student4", "Student5"]
)

print("\nPandas DataFrame:\n", df)

# -------------------------------
# Step 3: Perform analysis with Pandas
# -------------------------------

# Average marks per student
df["Average"] = df.mean(axis=1)

# Highest marks in each subject
highest_scores = df[["Math", "Science", "English"]].max()

# Class average per subject
class_avg = df[["Math", "Science", "English"]].mean()

print("\nAverage per student:\n", df["Average"])
print("\nHighest score in each subject:\n", highest_scores)
print("\nClass average per subject:\n", class_avg)
