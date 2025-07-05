import yfinance as yf
import datetime
import numpy as np
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import root_mean_squared_error, r2_score, mean_absolute_percentage_error
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

#define our forecasting gunction
def forecast(df, model, xscaler, yscaler,xscale):    
#def forecast(df, model, xscaler, yscaler,xscale):    

    
    from datetime import timedelta
    import numpy as np
    #Need a recent CAGR For our Forecasting Trend:
    lookback_days = 1260 
    recent_data = df.iloc[-lookback_days:]
    start_price = recent_data['Close'].iloc[-400]
    end_price = recent_data['Close'].iloc[-1]
    years = (recent_data.index[-1] - recent_data.index[0]).days / 365
    cagr = (end_price / start_price) ** (1 / years) - 1
    log_cagr = np.log(1 + cagr)
    
    #We need a list of opening prices that our forecasting will work on
    pricehist = df['Open'].iloc[-500:]
    pricehist = list(pricehist)
    forecast_features = [
                        'Weekday', 'Month', 'Open', "Years_Since_Start", "Days_Since_Start", "SMA_200", "SMA_500", 'sin_1', 'sin_2','sin_3', 'sin_4', 'cos_1', 'cos_2','cos_3', 'cos_4'
        ]
    window = 252
    forecast_days = 2520

    #use some of our old data
    feature_hist = xscale[-window:] 
    last_day_count = df['Days_Since_Start'].iloc[-1]
    total_years = df['Years_Since_Start'].iloc[-1]
    date = df.index[-1]
    SMA_200 = np.mean(pricehist[-200:])
    SMA_500 = np.mean(pricehist[-500:])
    future_dates = []
    pred_log = []
    pred_price = []

    progress_bar = st.progress(0)

    #create a daily trend variable to add a trend to the data 

    for i in range(forecast_days):
        t = len(df) + i + 1

        #NEED this if statement, otherwise our first day dramatically trends downward on the first forecasted day, we will just append the last close price & not do anything else
        if i < 3:
            date += timedelta(days=1)
            while date.weekday() > 4:
                date += timedelta(days=1)

            log_scaled = model.predict(feature_hist.reshape(1, window, -1))[0, 0]
            log_real = yscaler.inverse_transform([[log_scaled]])[0, 0]

            #Blend log prediction with real last log price (weighted average)
            last_log = np.log(df['Close'].iloc[-1])
            log_real_blend =  last_log  #no blend, need to append last close price 

            pred_log.append(log_real_blend)
            pred_price.append(np.exp(log_real_blend))
            future_dates.append(date)
            continue

        #skip non trading days
        date += timedelta(days=1)
        while date.weekday() > 4:
            date += timedelta(days=1) 

        #pricehist = Tickerdata['Open'].iloc[-500:]
        # Reshape our data for LSTM
        LSTM_input = feature_hist.reshape(1, window, -1)
        log_scaled = model.predict(LSTM_input)[0, 0]


        #transform our target
        log_real = yscaler.inverse_transform([[log_scaled]])[0, 0]

        #adding our CAGR Trend
        log_real_trend = log_real + log_cagr * i / 252
        pred_log.append(log_real_trend)


        #exponentiate to list of predictions in dollars


        #####################################################
        price = float(np.exp(log_real_trend))#cast to float to avoid error
       # price = float(np.exp(log_real))
        pred_price.append(price)
        pricehist.append(price)
        pricehist = pricehist[-500:]

        #redefine these features to be used meaningfully inside our loop
        SMA_200 = np.mean(pricehist[-200:])
        SMA_500=  np.mean(pricehist[-500:])
        #volatility = np.std(pricehist[-200:])
        #append next trading day to 
        future_dates.append(date) 

        #Generate next row using predicted price as Open
        year = total_years + (i+1) / 252
        new_row = {
            'Weekday':date.weekday(),
            'Month': date.month,
            'Open': price,
            'Year': date.year,
            'Years_Since_Start': year,
            'Days_Since_Start': last_day_count + i + 1,   
            'SMA_200':SMA_200,
            'SMA_500':SMA_500,
        }
        progress = i/forecast_days
        progress_bar.progress(progress)

        new_row['sin_1'] = np.sin(2*np.pi* 1 * t / 252)
        new_row['cos_1'] = np.cos(2*np.pi* 1 * t / 252)   

        new_row['sin_2'] = np.sin(2*np.pi* 2 * t / 252)
        new_row['cos_2'] = np.cos(2*np.pi* 2 * t / 252)

        new_row['sin_3'] = np.sin(2*np.pi* 4 * t / 252)
        new_row['cos_3'] = np.cos(2*np.pi* 4 * t / 252)

        new_row['sin_4'] = np.sin(2*np.pi* 4 * t / 252)
        new_row['cos_4'] = np.cos(2*np.pi* 4 * t / 252)


        #create array of features
        new_vals_df = pd.DataFrame([new_row], columns=forecast_features)
        new_scaled = xscaler.transform(new_vals_df)

        #  Update window
        feature_hist = np.vstack([feature_hist, new_scaled])[-window:]
    progress_bar.empty()
    forecast_df = pd.DataFrame({
        'Date':future_dates,
        'Log_Close_Pred': pred_log,
        'Close_Pred': pred_price
    }).set_index('Date')

    
    return forecast_df, pred_price



#define our forecasting gunction
def forecastbear(df, model, xscaler, yscaler,xscale, scale_factor):    
#def forecastbear(df, model, xscaler, yscaler,xscale):    
    
    from datetime import timedelta
    import numpy as np
    #Need a recent CAGR For our Forecasting Trend:
    lookback_days = 1260 
    recent_data = df.iloc[-lookback_days:]
    start_price = recent_data['Close'].iloc[-400]
    end_price = recent_data['Close'].iloc[-1]
    years = (recent_data.index[-1] - recent_data.index[0]).days / 365
    cagr = (end_price / start_price) ** (1 / years) - 1
    log_cagr = np.log(1 + cagr)
    
    #We need a list of opening prices that our forecasting will work on
    pricehist = df['Open'].iloc[-500:]
    pricehist = list(pricehist)
    forecast_features = [
                        'Weekday', 'Month', 'Open', "Years_Since_Start", "Days_Since_Start", "SMA_200", "SMA_500", 'sin_1', 'sin_2','sin_3', 'sin_4', 'cos_1', 'cos_2','cos_3', 'cos_4'
        ]
    window = 252
    forecast_days = 2520

    #use some of our old data
    feature_hist = xscale[-window:] 
    last_day_count = df['Days_Since_Start'].iloc[-1]
    total_years = df['Years_Since_Start'].iloc[-1]
    date = df.index[-1]
    SMA_200 = np.mean(pricehist[-200:])
    SMA_500 = np.mean(pricehist[-500:])
    future_dates = []
    pred_log = []
    pred_price = []


    #create a daily trend variable to add a trend to the data 

    for i in range(forecast_days):
        t = len(df) + i + 1

        #NEED this if statement, otherwise our first day dramatically trends downward on the first forecasted day, we will just append the last close price & not do anything else
        if i ==0:
            date += timedelta(days=1)
            while date.weekday() > 4:
                date += timedelta(days=1)

            log_scaled = model.predict(feature_hist.reshape(1, window, -1))[0, 0]
            log_real = yscaler.inverse_transform([[log_scaled]])[0, 0]

            #Blend log prediction with real last log price (weighted average)
            last_log = np.log(df['Close'].iloc[-1])
            log_real_blend = last_log #no blend, need to append last close price 

            
            # log_real_trend = log_real_blend  # no CAGR yet

            pred_log.append(log_real_blend)
            pred_price.append(np.exp(log_real_blend))
            future_dates.append(date)
            continue

        #skip non trading days
        date += timedelta(days=1)
        while date.weekday() > 4:
            date += timedelta(days=1) 

        #pricehist = Tickerdata['Open'].iloc[-500:]
        # Reshape our data for LSTM
        LSTM_input = feature_hist.reshape(1, window, -1)
        log_scaled = model.predict(LSTM_input)[0, 0]


        #transform our target
        log_real = yscaler.inverse_transform([[log_scaled]])[0, 0]

        #adding our CAGR Trend
        log_real_trend = log_real + log_cagr * i / 252
        pred_log.append(log_real_trend)


        #exponentiate to list of predictions in dollars


        #####################################################
        price = float(np.exp(log_real_trend))#cast to float to avoid error
       # price = float(np.exp(log_real))
        pred_price.append(price * scale_factor )
        pricehist.append(price * scale_factor)
        #pred_price.append(price )
        #pricehist.append(price )
        pricehist = pricehist[-500:]

        #redefine these features to be used meaningfully inside our loop
        SMA_200 = np.mean(pricehist[-200:])
        SMA_500=  np.mean(pricehist[-500:])
        #volatility = np.std(pricehist[-200:])
        #append next trading day to 
        future_dates.append(date) 

        #Generate next row using predicted price as Open
        year = total_years + (i+1) / 252
        new_row = {
            'Weekday':date.weekday(),
            'Month': date.month,
            'Open': price,
            'Year': date.year,
            'Years_Since_Start': year,
            'Days_Since_Start': last_day_count + i + 1,   
            'SMA_200':SMA_200,
            'SMA_500':SMA_500,
        }


        new_row['sin_1'] = np.sin(2*np.pi* 1 * t / 252)
        new_row['cos_1'] = np.cos(2*np.pi* 1 * t / 252)   

        new_row['sin_2'] = np.sin(2*np.pi* 2 * t / 252)
        new_row['cos_2'] = np.cos(2*np.pi* 2 * t / 252)

        new_row['sin_3'] = np.sin(2*np.pi* 4 * t / 252)
        new_row['cos_3'] = np.cos(2*np.pi* 4 * t / 252)

        new_row['sin_4'] = np.sin(2*np.pi* 4 * t / 252)
        new_row['cos_4'] = np.cos(2*np.pi* 4 * t / 252)


        #create array of features
        new_vals_df = pd.DataFrame([new_row], columns=forecast_features)
        new_scaled = xscaler.transform(new_vals_df)

        #  Update window
        feature_hist = np.vstack([feature_hist, new_scaled])[-window:]
    
    forecast_df = pd.DataFrame({
        'Date':future_dates,
        'Log_Close_Pred': pred_log,
        'Close_Pred': pred_price
    }).set_index('Date')


    return forecast_df, pred_price
