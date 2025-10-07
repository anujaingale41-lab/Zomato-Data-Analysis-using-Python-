import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# Histogram Plot
def plot_histogram(series, title, xlabel, ylabel, bins=20, save_path=None):
    """Plot a histogram with optional save."""
    plt.figure(figsize=(8,5))
    sns.histplot(series, bins=bins, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Bar Plot from Value Counts
def plot_top_categories(series, top_n=10, title='', xlabel='Count', ylabel='Category', palette='viridis', save_path=None):
    """Plot top N categories from a series."""
    top_values = series.value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_values.values, y=top_values.index, palette=palette)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Boxplot Comparison
def plot_boxplot(df, x_col, y_col, title='', xlabel='', ylabel='', save_path=None):
    """Plot a boxplot comparing two columns."""
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x=x_col, y=y_col)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Scatter Plot
def plot_scatter(df, x_col, y_col, title='', xlabel='', ylabel='', alpha=0.5, save_path=None):
    """Plot a scatter plot between two columns."""
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x=x_col, y=y_col, alpha=alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# Grouped Bar Plot
def plot_grouped_bar(df, group_col, value_col, agg_func='sum', top_n=10, title='', xlabel='Value', ylabel='Group', palette='mako', save_path=None):
    """Plot a grouped bar chart by aggregation."""
    grouped = df.groupby(group_col)[value_col].agg(agg_func).sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(10,6))
    sns.barplot(x=grouped.values, y=grouped.index, palette=palette)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
