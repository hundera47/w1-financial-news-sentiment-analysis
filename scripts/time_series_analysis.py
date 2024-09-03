import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TimeSeriesAnalysis:
    def __init__(self, news_file, stock_files):
        self.news_file = news_file
        self.stock_files = stock_files
        self.news_data = None
        self.stock_data = {}
        
    def load_data(self):
        # Load news data
        self.news_data = pd.read_csv(self.news_file)
        
        # Load stock data
        for file in self.stock_files:
            stock_symbol = file.split('/')[-1].replace('.csv', '')
            self.stock_data[stock_symbol] = pd.read_csv(file)
        
        # Display a message
        print("Data loaded successfully.")

    def preprocess_data(self):
        # Load the data
        self.news_data = pd.read_csv(self.news_file)
        
        # Check and print column names to verify correct naming
        print("Columns in news data:", self.news_data.columns)
        
        # Strip any leading/trailing spaces from column names
        self.news_data.columns = self.news_data.columns.str.strip()
        
        # Ensure the 'date' column exists before conversion
        if 'date' in self.news_data.columns:
            # Convert 'date' column to datetime, inferring format and timezone
            self.news_data['date'] = pd.to_datetime(self.news_data['date'], errors='coerce')
        else:
            raise KeyError("Column 'date' not found in news data.")
        
        # Rename columns in stock data and convert date columns
        for symbol, data in self.stock_data.items():
            # Check and print column names to verify correct naming
            print(f"Columns in {symbol} stock data:", data.columns)
            
            # Strip any leading/trailing spaces from column names
            data.columns = data.columns.str.strip()
            
            # Ensure the 'Date' column exists before conversion
            if 'Date' in data.columns:
                data.rename(columns={'Date': 'date'}, inplace=True)
                data['date'] = pd.to_datetime(data['date'], errors='coerce')
            else:
                raise KeyError(f"Column 'Date' not found in {symbol} stock data.")
            
            # Drop rows with invalid dates
            data.dropna(subset=['date'], inplace=True)
        
        print("Data preprocessed successfully.")


    def analyze_publication_frequency(self):
        # Count articles per day
        daily_counts = self.news_data.groupby(self.news_data['date'].dt.date).size()
        
        # Plot publication frequency
        plt.figure(figsize=(12, 6))
        daily_counts.plot()
        plt.title('Publication Frequency Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.grid(True)
        plt.show()

    def analyze_publishing_times(self):
        # Extract publishing hour
        self.news_data['hour'] = self.news_data['date'].dt.hour
        
        # Count articles per hour
        hourly_counts = self.news_data.groupby('hour').size()
        
        # Plot publishing times
        plt.figure(figsize=(12, 6))
        hourly_counts.plot(kind='bar')
        plt.title('Number of Articles Published by Hour of the Day')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Number of Articles')
        plt.grid(True)
        plt.show()

    def merge_news_stock_data(self):
        # Ensure the 'date' column in news data is in datetime format with UTC timezone
        if 'date' in self.news_data.columns:
            self.news_data['date'] = pd.to_datetime(self.news_data['date'])
            if self.news_data['date'].dt.tz is None:
                self.news_data['date'] = self.news_data['date'].dt.tz_localize('UTC')
            else:
                self.news_data['date'] = self.news_data['date'].dt.tz_convert('UTC')
            
            # Drop rows with NaT values in 'date' column
            self.news_data = self.news_data.dropna(subset=['date'])
        else:
            raise KeyError("Column 'date' not found in news data.")
        
        self.merged_data = {}  # Initialize the attribute to store merged data

        for symbol, data in self.stock_data.items():
            if 'date' in data.columns:
                data['date'] = pd.to_datetime(data['date'])
                if data['date'].dt.tz is None:
                    data['date'] = data['date'].dt.tz_localize('UTC')
                else:
                    data['date'] = data['date'].dt.tz_convert('UTC')
                
                # Drop rows with NaT values in 'date' column
                data = data.dropna(subset=['date'])
            else:
                raise KeyError(f"Column 'date' not found in {symbol} stock data.")
            
            # Merge news data with stock data
            self.merged_data[symbol] = pd.merge_asof(self.news_data.sort_values('date'), 
                                                    data.sort_values('date'), 
                                                    on='date')
            
            print(f"Merged data for {symbol}:")
            print(self.merged_data[symbol].head())

        print("Data merged successfully.")



if __name__ == "__main__":
    # Define file paths
    news_file = '../data/raw_analyst_ratings.csv'
    stock_files = [f'../data/yfinance_data/{file}' for file in ['AAPL.csv', 'AMZN.csv', 'GOOG.csv', 'META.csv', 'MSFT.csv', 'NVDA.csv', 'TSLA.csv']]
    
    # Create an instance of the TimeSeriesAnalysis class
    tsa = TimeSeriesAnalysis(news_file, stock_files)
    
    # Load and preprocess data
    tsa.load_data()
    tsa.preprocess_data()
    
    # Perform analyses
    tsa.analyze_publication_frequency()
    tsa.analyze_publishing_times()
    tsa.merge_news_stock_data()
