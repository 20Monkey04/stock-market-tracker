# Predictions


# Imports

import pandas as pd
import datetime
from sklearn.linear_model import LinearRegression

# =========================================

# Predict Next Close

def predict_next_close(df):
    
    df = df.reset_index()
    df['DateOrdinal'] = pd.to_datetime(df['Date']).map(datetime.datetime.toordinal)
    X = df['DateOrdinal'].values.reshape(-1,1)
    y = df['Close'].values
    model = LinearRegression()
    model.fit(X, y)
    next_day = df['DateOrdinal'].max() + 1
    pred = model.predict([[next_day]])
    
    return pred[0]