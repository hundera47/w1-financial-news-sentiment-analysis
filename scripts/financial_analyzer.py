# scripts/financial_analyzer.py

import pandas as pd

class FinancialAnalyzer:
    def __init__(self):
        # Add any necessary initialization parameters
        pass

    def load_news_data(self, file_path):
        """
        Load and prepare the financial news data.
        
        Parameters:
        file_path (str): The path to the financial news dataset CSV file.
        
        Returns:
        pd.DataFrame: A DataFrame containing the prepared news data.
        """
        # Load the dataset
        df = pd.read_csv(file_path)

        # Parse dates and allow pandas to infer the correct format
        df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

        # Extract time components if needed
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day

        return df
