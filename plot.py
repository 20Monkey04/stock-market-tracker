# Plot


# Imports


import matplotlib.pyplot as plt


# =========================================

# Plot Chart

def plot_chart(df, ticker, stop_loss, take_profit):
    
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.plot(df.index, df['MA5'], label='MA5')
    plt.plot(df.index, df['MA20'], label='MA20')

    buys = df[df['Signal'] == 1]
    sells = df[df['Signal'] == -1]
    plt.scatter(buys.index, buys['Close'], marker='^', color='g', label='Buy Signal', s=100)
    plt.scatter(sells.index, sells['Close'], marker='v', color='r', label='Sell Signal', s=100)

    plt.axhline(stop_loss, color='r', linestyle='--', label='Stop Loss')
    plt.axhline(take_profit, color='g', linestyle='--', label='Take Profit')

    plt.title(f'{ticker} Price Chart with Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()