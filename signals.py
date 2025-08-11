# Stock Signals


# Imports

import pandas as pd



# =========================================

# Generate Signals

def generate_signals(df):
    
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['Signal'] = 0
    df.loc[df['MA5'] > df['MA20'], 'Signal'] = 1   # Buy
    df.loc[df['MA5'] < df['MA20'], 'Signal'] = -1  # Sell
    
    return df

# Calculate Stop Loss / Take Profit

def calculate_stop_loss_take_profit(df):
    
    last_close = df['Close'].iloc[-1]
    stop_loss = last_close * 0.97
    take_profit = last_close * 1.06
    
    return stop_loss, take_profit