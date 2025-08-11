# Save


# Imports


import pandas as pd


# =========================================

# Save To Excel

def save_to_excel(df, ticker):
    import pandas as pd

   
    if pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = df.index.tz_localize(None)

   
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    filename = f"{ticker}_data.xlsx"
    df.to_excel(filename)
    print(f"Saved data to {filename}")

