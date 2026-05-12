from fastapi import FastAPI

import pandas as pd


# ==============================
# CREATE API APP
# ==============================

app = FastAPI()


# ==============================
# LOAD FORECAST DATA
# ==============================

forecast_df = pd.read_csv(
    'future_forecasts.csv'
)


# ==============================
# HOME ROUTE
# ==============================

@app.get('/')

def home():

    return {

        'message':
        'Forecasting API Running Successfully'

    }


# ==============================
# FORECAST ROUTE
# ==============================

@app.get('/forecast')

def get_forecast():

    return forecast_df.to_dict(
        orient='records'
    )