import pandas as pd

def calculate_headline_length(df):
    """
    Calculate the length of headlines in the dataset.

    Parameters:
    df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    pd.Series: Series with the length of each headline.
    """
    return df['headline'].apply(len)

def count_articles_per_publisher(df):
    """
    Count the number of articles per publisher.

    Parameters:
    df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    pd.Series: Series with counts of articles per publisher.
    """
    return df['publisher'].value_counts()

def plot_articles_over_time(df):
    """
    Plot the number of articles over time.

    Parameters:
    df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    None
    """
    df['date'] = pd.to_datetime(df['date'])
    df['date'].value_counts().sort_index().plot()
