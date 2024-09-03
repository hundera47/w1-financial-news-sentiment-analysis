# time_series_analyze.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def descriptive_statistics(data):
    """
    Computes and returns descriptive statistics of the dataset.
    
    Parameters:
    data (pd.DataFrame): The dataset to analyze.
    
    Returns:
    pd.DataFrame: Descriptive statistics of the dataset.
    """
    if isinstance(data, pd.DataFrame):
        return data.describe()
    else:
        raise TypeError("The input must be a pandas DataFrame.")

def plot_time_series(data, column='Close', title='Stock Price Over Time'):
    """
    Plots the time series of a specific column in the dataset.
    
    Parameters:
    data (pd.DataFrame): The dataset containing the time series data.
    column (str): The column name to plot. Defaults to 'Close'.
    title (str): The title of the plot. Defaults to 'Stock Price Over Time'.
    """
    if 'date' in data.columns and column in data.columns:
        plt.figure(figsize=(12, 6))
        plt.plot(data['date'], data[column], label=column, color='blue')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        raise KeyError("The dataset must contain 'date' and specified column.")

def plot_stock_price_distribution(data, column='Close', title='Stock Price Distribution'):
    """
    Plots the distribution of stock prices in the dataset.
    
    Parameters:
    data (pd.DataFrame): The dataset containing the stock price data.
    column (str): The column name to plot. Defaults to 'Close'.
    title (str): The title of the plot. Defaults to 'Stock Price Distribution'.
    """
    if column in data.columns:
        plt.figure(figsize=(12, 6))
        sns.histplot(data[column], kde=True, bins=30)
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        raise KeyError(f"The dataset must contain the column '{column}'.")

# Example usage
if __name__ == "__main__":
    # Sample usage with example data
    # Replace 'data' with your actual DataFrame
    data = pd.DataFrame({
        'date': pd.date_range(start='2020-01-01', periods=100),
        'Close': pd.np.random.rand(100) * 100
    })

    print(descriptive_statistics(data))
    plot_time_series(data)
    plot_stock_price_distribution(data)
