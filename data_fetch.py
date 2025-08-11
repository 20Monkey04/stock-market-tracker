# Data Fetch


# Imports

import requests
import yfinance as yf
import pandas as pd

from finvizfinance.insider import Insider
from io import StringIO


# =========================================

# Fetch Stock Data

def fetch_stock_data(ticker):
    
    stock = yf.Ticker(ticker)
    df = stock.history(period='6mo', interval='1d')
    return df, stock

# Get Insider Trades

def get_insider_trades(ticker):
    try:
        insider = Insider(ticker)
        # Try official method if exists
        if hasattr(insider, 'get_insider_trades'):
            df = insider.get_insider_trades()
            if not df.empty:
                return df
        # If no official method or empty, fallback
        return get_insider_trades_fallback(ticker)

    except Exception:
        # On any error, fallback to scraping
        return get_insider_trades_fallback(ticker)

    
# Fallback
    
def get_insider_trades_fallback(ticker):
    url = f"https://finviz.com/insidertrading.ashx?tc={ticker}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        tables = pd.read_html(StringIO(response.text))

        insider_table = None
        for table in tables:
            # Check if this table has the insider trades columns
            if set(['Date', 'Insider', 'Relationship', 'Transaction', 'Cost', 'Shares']).issubset(table.columns):
                insider_table = table
                break

        if insider_table is None or insider_table.empty:
            return pd.DataFrame()

        insider_table = insider_table.dropna(how='all')
        return insider_table

    except Exception:
        return pd.DataFrame()

    

