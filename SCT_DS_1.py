import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATASET
# -----------------------------

file_path = "/Users/chinthireddyakshara/Downloads/SCT_DS_1.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Dataset Loaded Successfully!")
print(df.head())

print("\nColumns in Dataset:")
print(df.columns.tolist())

# -----------------------------
# FIGURE 1 — Population Distribution
# -----------------------------

if 'Population' in df.columns:

    plt.figure(figsize=(8,5))

    population_data = pd.to_numeric(
        df['Population'],
        errors='coerce'
    ).dropna()

    plt.hist(
        population_data,
        bins=15,
        color='skyblue',
        edgecolor='black'
    )

    plt.title("Population Distribution")
    plt.xlabel("Population")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("population_distribution.png")
    plt.show()

else:
    print("Population column not found.")

# -----------------------------
# FIGURE 2 — Gender Distribution
# -----------------------------

if 'Gender' in df.columns:

    plt.figure(figsize=(6,4))

    sns.countplot(
        data=df,
        x='Gender',
        hue='Gender',
        palette='pastel',
        legend=False
    )

    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig("gender_distribution.png")
    plt.show()

else:
    print("Gender column not found.")

# -----------------------------
# FIGURE 3 — Region Distribution
# -----------------------------

if 'Region' in df.columns:

    plt.figure(figsize=(10,6))

    sns.countplot(
        data=df,
        y='Region',
        order=df['Region'].value_counts().index,
        palette='viridis'
    )

    plt.title("Region Distribution")
    plt.xlabel("Count")
    plt.ylabel("Region")

    plt.tight_layout()

    plt.savefig("region_distribution.png")
    plt.show()

else:
    print("Region column not found.")

# -----------------------------
# COMPLETION MESSAGE
# -----------------------------

print("\nTask completed successfully!")
print("Charts saved as:")
print("1. population_distribution.png")
print("2. gender_distribution.png")
print("3. region_distribution.png")