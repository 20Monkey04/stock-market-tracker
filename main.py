# Central Code (Main)


# Imports

from data_fetch import fetch_stock_data, get_insider_trades
from signals import generate_signals, calculate_stop_loss_take_profit
from prediction import predict_next_close
from news_fetch import get_news
from save import save_to_excel
from plot import plot_chart
import pandas as pd

# =========================================

# Main

def main():
    while True:
        ticker = input("Enter ticker symbol (or 'exit' to stop): ").upper()
        if ticker == 'EXIT':
            break

        try:
            df, stock = fetch_stock_data(ticker)
            if df.empty:
                print("No data found for this ticker.")
                continue

            df = generate_signals(df)

            pred_close = predict_next_close(df)
            print(f"Predicted next closing price for {ticker}: ${pred_close:.2f}")

            stop_loss, take_profit = calculate_stop_loss_take_profit(df)
            print(f"Suggested Stop Loss: ${stop_loss:.2f}, Take Profit: ${take_profit:.2f}")

            news = get_news(ticker)
            print(f"\nLatest news about {ticker}:")
            for title, url in news:
                print(f"- {title}\n  {url}")

            insider_trades = get_insider_trades(ticker)
            if not insider_trades.empty:
                print(f"\nRecent insider trades for {ticker}:")
                print(insider_trades.to_string(index=False))
            else:
                print("\nNo recent insider trades data available.")

            save_to_excel(df, ticker)
            plot_chart(df, ticker, stop_loss, take_profit)

        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")

if __name__ == "__main__":
    main()