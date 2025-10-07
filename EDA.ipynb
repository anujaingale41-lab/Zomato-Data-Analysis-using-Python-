# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# Step 2: Load and Clean Data
from src.clean_data import clean_zomato_data

# Adjust path if needed
df = clean_zomato_data('data/zomato.xlsx')
df.head()

# Step 3: Basic Info
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
df.info()
df.describe()
df.isnull().sum()

# Step 4: Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Rate'], bins=20, kde=True)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.tight_layout()
# plt.savefig('outputs/plots/rating_distribution.png')  # Optional
plt.show()

# Step 5: Top Restaurant Types
top_types = df['listed_in(type)'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_types.values, y=top_types.index, palette='viridis')
plt.title('Top 10 Restaurant Types')
plt.xlabel('Count')
plt.ylabel('Type')
plt.tight_layout()
# plt.savefig('outputs/plots/top_restaurant_types.png')
plt.show()

# Step 6: Online Order vs Rating
sns.boxplot(data=df, x='Has_Online_delivery', y='Rate')
plt.title('Online Delivery vs Rating')
plt.xlabel('Online Delivery Available')
plt.ylabel('Rating')
plt.tight_layout()
# plt.savefig('outputs/plots/online_delivery_vs_rating.png')
plt.show()

# Step 7: Cost vs Rating
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Cost', y='Rate', alpha=0.5)
plt.title('Cost vs Rating')
plt.xlabel('Approx Cost for Two')
plt.ylabel('Rating')
plt.tight_layout()
# plt.savefig('outputs/plots/cost_vs_rating.png')
plt.show()

# Step 8: Votes vs Restaurant Type
vote_by_type = df.groupby('listed_in(type)')['Vote_Count'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=vote_by_type.values, y=vote_by_type.index, palette='mako')
plt.title('Votes by Restaurant Type')
plt.xlabel('Total Votes')
plt.ylabel('Type')
plt.tight_layout()
# plt.savefig('outputs/plots/votes_by_type.png')
plt.show()

# Step 9: Cuisines Breakdown (Optional)
cuisine_counts = df['Cuisines'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=cuisine_counts.values, y=cuisine_counts.index, palette='cubehelix')
plt.title('Top 10 Cuisines')
plt.xlabel('Count')
plt.ylabel('Cuisine')
plt.tight_layout()
# plt.savefig('outputs/plots/top_cuisines.png')
plt.show()

# Step 10: Save Summary (Optional)
df.describe().to_csv('outputs/summary.csv')
