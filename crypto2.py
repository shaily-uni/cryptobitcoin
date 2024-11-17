import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def fetch_crypto_data(crypto_symbol, start_date, end_date):
    data = yf.download(crypto_symbol, start=start_date, end=end_date)
    data.index = data.index.date
    
    return data
# Calculate moving average for prediction
def moving_average_prediction(data, window_size):
    data['Moving_Avg'] = data['Close'].rolling(window=window_size).mean()
    return data

# Visualize cryptocurrency prices and moving average
def plot_crypto_data(data, crypto_name, window_size):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Actual Price', color='blue')
    
    # Plot moving average after the first 'window_size' days, avoiding NaN values
    plt.plot(data.index[window_size-1:], data['Moving_Avg'][window_size-1:], label=f'{window_size}-Day Moving Average', color='orange')
    
    plt.title(f'{crypto_name} Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main program
if __name__ == "__main__":
    # Input parameters
    crypto_symbol = "BTC-USD"  # Example: Bitcoin (BTC)
    start_date = "2024-01-01"
    end_date = "2024-11-16"
    window_size = 30  # Moving average window size

    # Fetch data
    crypto_data = fetch_crypto_data(crypto_symbol, start_date, end_date)

    # Display the first few rows of the fetched data
    print("Fetched cryptocurrency data:")
    print(crypto_data.head())  # Shows the first 5 rows

    # Predict using moving average
    predicted_crypto_data = moving_average_prediction(crypto_data, window_size)

    # Plot results
    plot_crypto_data(predicted_crypto_data, crypto_symbol, window_size)
