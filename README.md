End-to-End Time Series Forecasting System

Objective
Build a production-ready forecasting system that:
- trains multiple forecasting models
- compares and selects the best model
- forecasts future sales
- exposes predictions through REST API

Models Implemented
1. SARIMA
2. Facebook Prophet
3. XGBoost
4. LSTM

features Engineered
- Lag Features
- Rolling Mean
- Rolling Standard Deviation
- Month Feature
- Quarter Feature
- Year Feature

Workflow
1. Data Cleaning
2. Missing Date Handling
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Best Model Selection
7. Future Forecasting
8. FastAPI Deployment

API Endpoints

Home
/
Forecast
/forecast

Technologies Used
- python
- Pandas
- Statsmodels
- Prophet
- XGBoost
- TensorFlow
- FastAPI

Output
The system forecasts future sales and serves predictions through REST API.
