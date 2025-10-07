import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# Rating Distribution
def plot_rating_distribution(df, save_path=None):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Rate'], bins=20, kde=True)
    plt.title('Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Top Restaurant Types
def plot_top_restaurant_types(df, top_n=10, save_path=None):
    top_types = df['listed_in(type)'].value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_types.values, y=top_types.index, palette='viridis')
    plt.title(f'Top {top_n} Restaurant Types')
    plt.xlabel('Count')
    plt.ylabel('Type')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Online Delivery vs Rating
def plot_online_delivery_vs_rating(df, save_path=None):
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x='Has_Online_delivery', y='Rate')
    plt.title('Online Delivery vs Rating')
    plt.xlabel('Online Delivery Available')
    plt.ylabel('Rating')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Cost vs Rating
def plot_cost_vs_rating(df, save_path=None):
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x='Cost', y='Rate', alpha=0.5)
    plt.title('Cost vs Rating')
    plt.xlabel('Approx Cost for Two')
    plt.ylabel('Rating')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Votes by Restaurant Type
def plot_votes_by_type(df, top_n=10, save_path=None):
    vote_by_type = df.groupby('listed_in(type)')['Vote_Count'].sum().sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(10,6))
    sns.barplot(x=vote_by_type.values, y=vote_by_type.index, palette='mako')
    plt.title(f'Votes by Restaurant Type (Top {top_n})')
    plt.xlabel('Total Votes')
    plt.ylabel('Type')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Top Cuisines
def plot_top_cuisines(df, top_n=10, save_path=None):
    cuisine_counts = df['Cuisines'].value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    sns.barplot(x=cuisine_counts.values, y=cuisine_counts.index, palette='cubehelix')
    plt.title(f'Top {top_n} Cuisines')
    plt.xlabel('Count')
    plt.ylabel('Cuisine')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
