import yfinance as yf
import pandas as pd
from app.models.models import Tickers


async def get_stock_data_from_api(ticker_data_to_get: Tickers) -> pd.DataFrame:
    """All stock data is retrieved from Yahoo Finance API  with a 1 hr interval"""
    stock_data = yf.Ticker(ticker_data_to_get.ticker)
    history = stock_data.history(
        period="1d", start=ticker_data_to_get.date_from, end=ticker_data_to_get.date_to
    )
    return history
