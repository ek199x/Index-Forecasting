# necessary imports

import streamlit as st
from datetime import timedelta
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import root_mean_squared_error, r2_score, mean_absolute_percentage_error
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import pandas as pd
import joblib

from forecasters import forecast as main_forecast
#Interactive User Interface Elements
st.set_page_config(initial_sidebar_state="expanded")
st.title('Stock Forecasting Project - Eduard Klyuchinskiy')
st.sidebar.title('Choose Your Fund')
funds = st.sidebar.selectbox('fund',['S&P 500', 'DOW JONES', 'NASDAQ'])
submit = st.sidebar.button('submit')
st.header(f'Your chosen fund: {funds}')

#Define Time Series variables that will be used in our DF generation
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
twenty_years = 365*20
past_20 = today - datetime.timedelta(days=twenty_years)


if funds == 'S&P 500':
    ticker = '^GSPC'
    st.write('The S&P 500 Index is a list of 500 of the largest public companies in the U.S. These companies are the biggest and most important companies in the country, and represent a broad cross-section of the economy. It is managed by S&P Dow Jones Indices, a subsidiary of S&P Global. The index, which is weighted by market capitalization, is considered to be one of the best gauges of U.S. equities, the stock market, and the American economy. https://www.investopedia.com/terms/s/sp500.asp.')
    mpath= 'models/GSPC/'
    vpath= 'visuals/GSPC/'
if funds == 'DOW JONES':
    ticker = '^DJI'
    st.write("The Dow Jones Industrial Average (DJIA) tracks thirty of America's biggest and most established companies, acting like a quick temperature check of the U.S. economy. https://www.investopedia.com/terms/d/djia.asp")
    mpath = 'models/DJI/'
    vpath = 'visuals/DJI/'
if funds == 'NASDAQ':
    ticker ='^IXIC'
    st.write('Nasdaq is a global electronic marketplace for buying and selling securities. Its name was originally an acronym for the National Association of Securities Dealers Automated Quotations. Nasdaq started as a subsidiary of the National Association of Securities Dealers (NASD), now known as the Financial Industry Regulatory Authority (FINRA). https://www.investopedia.com/terms/n/nasdaq.asp ')
    mpath = 'models/IXIC/'
    vpath = 'visuals/IXIC/'

def load_model():

    main = tf.keras.models.load_model(f'{mpath}main.keras')
    #bear = tf.keras.models.load_model(f'{mpath}bear.keras')
    xscaler = joblib.load(f'{mpath}xscaler.pkl')
    yscaler = joblib.load(f'{mpath}yscaler.pkl')
    xscale = joblib.load(f'{mpath}xscale.pkl')
    #bearfig = joblib.load(f'{vpath}bear_fig.pkl')
    #bearsum = joblib.load(f'{vpath}bear_summary.pkl')
    mainfig = joblib.load(f'{vpath}main_fig.pkl')
    mainsum = joblib.load(f'{vpath}main_summary.pkl')

#    return main,bear, xscaler, yscaler, xscale, bearfig, bearsum, mainfig, mainsum
    return main, xscaler, yscaler, xscale, mainfig, mainsum

#main, bear, xscaler, yscaler, xscale, bearfig, bearsum,mainfig, mainsum = load_model()
main, xscaler, yscaler, xscale,mainfig, mainsum = load_model()


def gen_df(begin_year, end_year, ticker):
    #prompt user for ticker
    ticker = ticker.upper()
    df = yf.download(ticker, start = begin_year, end = end_year) 
    df = df.xs(ticker, axis=1, level= 'Ticker')
    #Validates that a ticker has populated the DF
    while len(df) == 0:
        ticker = input("Invalid")
        ticker = ticker.upper()
        df = yf.download(ticker, start = begin_year , end = end_year) 
        df = df.xs(ticker, axis=1, level= 'Ticker')

    #Feature engineering

    #Add features based on the Date
    df['Weekday'] = df.index.day_of_week
    df['Month'] = df.index.month
    df['Year'] = df.index.year
    df['Days_Since_Start'] = (df.index - df.index[0]).days #days since start tracking
    df['Years_Since_Start'] = df['Days_Since_Start']/365
    return df

df = gen_df(past_20,yesterday, ticker)
#bear_data = gen_df(bear_start, bear_end,ticker)
#modern_avg = df['Close'].mean()
#bear_avg = bear_data['Close'].mean()


#modern_avg = df['Close'].mean()

def engineer_features(df):
    df['Log_Close'] = np.log(df['Close'])
    df['SMA_30'] = df['Close'].rolling(window = 30).mean()
    df['SMA_200'] = df['Close'].rolling(window = 200).mean() #200 day moving average using the rolling function, will create NANS that we will drop
    df['SMA_500'] = df['Close'].rolling(window = 500).mean()
    df['volatility'] = df['Close'].rolling(window=200).std()
    return df
df = engineer_features(df)
def add_fourier_terms(df, period=252, ): #adding 4 terms helped create a good shape for the LSTM, orginally only wanted sin, cos of 1, 2, and 4, but adding three helped smooth final DF generated out
    t = np.arange(len(df))
    df['sin_1'] = np.sin(2 * np.pi * 1 * t / period) 
    df['cos_1'] = np.cos(2 * np.pi * 1 * t / period)
    df['sin_2'] = np.sin(2 * np.pi * 2 * t / period) 
    df['cos_2'] = np.cos(2 * np.pi * 2 * t / period)
    df['sin_3'] = np.sin(2 * np.pi * 3 * t / period) 
    df['cos_3'] = np.cos(2 * np.pi * 3 * t / period)
    df['sin_4'] = np.sin(2 * np.pi * 4 * t / period) 
    df['cos_4'] = np.cos(2 * np.pi * 4 * t / period)
    return df
df = add_fourier_terms(df)
#Drop NA values
df.dropna(inplace=True)

st.header(f'{funds} timeline')
fig,ax = plt.subplots()
fig.patch.set_facecolor("#191729")
ax.set_facecolor('#191728')
ax.plot(df['Close'], color = 'white')
ax.set_xlabel('Time in Years', color = 'green', fontweight = 'bold')
ax.set_ylabel('Price in $', color = 'green', fontweight = 'bold')
ax.tick_params(axis='x',colors = 'green')
ax.tick_params(axis='y',colors = 'green')

initial_price = round(df['Close'].iloc[0],2)
last_price = round(df['Close'].iloc[-1],2)
ax.annotate(f'${initial_price} Initial Price',
            xy=(df.index[0] , initial_price),
            xytext=(df.index[0], initial_price * 1.5 ),
            arrowprops=dict(arrowstyle='simple'),
            fontsize=10,
            color = 'green',
            fontweight = 'bold')
ax.annotate(f'${last_price} last price',
            xy=(df.index[-1],last_price),
            xytext = (df.index[-1],last_price - last_price*.3),
            arrowprops=dict(arrowstyle='simple'),
            fontsize = 10,
            color = 'red',
            fontweight = 'bold')
ax.fill_between(df.index, df['Close'], color = 'black')
st.pyplot(fig)

#col1,col2, = st.columns(2)

RMSE_mainsum = round(mainsum['RMSE'],2)
R2_mainsum = round(mainsum['R2'],2)
MAPE_mainsum = round (mainsum['MAPE']*100,2)



#RMSE_bearsum = round(bearsum['RMSE'],2)    
#R2_bearsum = round(bearsum['R2'],2)

#MAPE_bearsum = round (bearsum['MAPE']*100,2)

st.markdown('#### Recent Data Model')
st.write(funds)
st.pyplot(mainfig)
st.markdown(f"""
The Recent Data Model is a Long Short Term Memory model trained on stock data spanning
the past 20 years up to the last logged day with a close price for the stock from the day of model training.
    
**\\${RMSE_mainsum:.2f}** was the root mean squared error in the recent data model,  
which means the predictions the model was making were off by **\\${RMSE_mainsum:.2f}** on average.

**{R2_mainsum:.3f}** was the R squared value for this model.  
This means that the model was able to explain **{R2_mainsum * 100:.2f}%** of the variance seen in the actual results.
    
**{MAPE_mainsum}**% Was the Mean Absolute Percentage Error for this model.
This means that the predictions of the model were off by {MAPE_mainsum}%
""")


if submit:
    submit = st.write('function running')
    df = gen_df(past_20, yesterday,ticker)
    df = engineer_features(df)
    df = add_fourier_terms(df)
    df.dropna(inplace=True)
    running = st.session_state.get("running", False)


    with st.spinner('Forecast Generating Stock Prices for the next Decade, this will take a little over 5 minutes.'):
      forecast_df,pred_price = main_forecast(df, main, xscaler, yscaler, xscale)
      #forecast_df,pred_price = forecast_func(df, selected_scenario, xscaler, yscaler, xscale)

   
    st.header('Decade Forecast')
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#191729")
    ax.set_facecolor('#191728')
    ax.plot(forecast_df['Close_Pred'], color = 'white')
    ax.set_xlabel('Time in Years', color = 'green', fontweight = 'bold')
    ax.set_ylabel('Price in $', color = 'green', fontweight = 'bold')
    ax.tick_params(axis='x',colors = 'green')
    ax.tick_params(axis='y',colors = 'green')
    initial_price = round(forecast_df['Close_Pred'].iloc[0],2)
    last_price = round(forecast_df['Close_Pred'].iloc[-1],2)
    ax.annotate(f'${initial_price} Initial Price',
            xy=(forecast_df.index[0] , initial_price),
            xytext=(forecast_df.index[0], initial_price *1.25),
            arrowprops=dict(arrowstyle='simple'),
            fontsize=10,
            color = 'green',
            fontweight = 'bold')
    ax.annotate(f'${last_price} last price',
            xy=(forecast_df.index[-1],last_price),
            xytext = (forecast_df.index[-1],last_price - (last_price*.25)),
            arrowprops=dict(arrowstyle='simple'),
            fontsize = 10,
            color = 'red',
            fontweight = 'bold')
    ax.fill_between(forecast_df.index, forecast_df['Close_Pred'], color = 'black')

    st.pyplot(fig)
    
    years = len(forecast_df)/365
    CAGR = round(((last_price / initial_price) **(1 / years) - 1 )*100)
    st.write(f'Your inital Price was {initial_price}, the last price was {last_price} that gives you a Compound Annual Growth Rate of {CAGR}%')
