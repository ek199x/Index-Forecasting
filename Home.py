import streamlit as st
import matplotlib.pyplot as plt
import joblib

st.set_page_config(page_title = 'Home')
st.title('Welcome To My Stock Forecasting Project')

SPSummary= joblib.load('SPSummary.pkl')
IXICSummary = joblib.load('IXICSummary.pkl')
DJISummary = joblib.load('DJISummary.pkl')

SPmean = round (SPSummary['mean'],2)
SPmin = round (SPSummary['min'],2)
SPmax = round (SPSummary['max'],2)
SPmed = round (SPSummary['50%'],2)
SPstd = round (SPSummary['std'],2)

IXmean = round (IXICSummary['mean'],2)
IXmin = round (IXICSummary['min'],2)
IXmax = round (IXICSummary['max'],2)
IXmed = round (IXICSummary['50%'],2)
IXstd = round (IXICSummary['std'],2)

DJImean = round (DJISummary['mean'],2)
DJImin = round (DJISummary['min'],2)
DJImax = round (DJISummary['max'],2)
DJImed = round (DJISummary['50%'],2)
DJIstd = round (DJISummary['std'],2)


st.markdown(
'''
My name is Eduard Klyuchinskiy and this is my Capstone Project for my Data Science Masters Program at Eastern University.

## About Me

    Currently I am in my final semester of my Masters program and am thoroughly enjoying learning all about data science. 
Especially the machine learning portion of the course. Throughout my time in the program I've learned so much about
both the math side and programming side of software, to the point where I think I have a solid understanding of how 
many websites and programs work,at least a little bit, behind the scenes. 
    My job in the U.S. Air Force is also very much related to data such as cleaning it,
processing it, and extracting insights out of it, so I've taken a lot of what I've learned from this course and have been able to
apply it to my job. For example, I was able to build a SQL database using microsoft access and link that database to PowerBI
and sharepoint in order to streamline a lot of the manual processes that existed in my workplace beforehand. 
    In my freetime(the little of it that I have) I am a huge videogame nerd, but who isn't these days? I also love going on hikes
running, and traveling. I'm originally from New York and I intend to go back after completing my service with the military. 
I'm hoping that during my transition I'll be able to utilize projects such as this as well as my resume and skills I've developed
to find myself a potential career that I can thrive in.

## About the Project

I wanted to make a project that would encourage people to invest into the economy over a long term period of time (like 10 years)
In order to do so, my idea was to create a project that forecasts the price of index funds 10 years int othe future and return
a CAGR (Compound Annual Growth Rate). What sets aside my forecasting project from many other ones you'll see online is that the forecasters online
act more like a calculator where you plug in a number, a percentage rate, and it will give you a return in the end, my project
used a Deep Learning model called 'Long Short Term Memory' to train over 20 years of stock data. With this in mind, the Long Short Term 
Memory by its design gives a larger weight to more recent data, which is why I picked this model so that in my forecast the model can 
pick up where it left off training, as a forecaster making predictions. 
'''

)

st.header('Data Exploration')

distribution = joblib.load('Distribution.pkl')
st.pyplot(distribution)


col1 , col2, col3 = st.columns(3)

col1.header('S&P 500')
col1.markdown('### Summary Statistics')
col1.markdown(
f'''
In the past twenty years the S&P 500 had these summary stats: 

minimum -**{SPmin}** 

maximum - **{SPmax}** 

median - **{SPmed}**

mean - **{SPmean}**

standard deviation - **{SPstd}** 
'''

)


col2.header('DOW JONES')
col2.markdown('### Summary Statistics')
col2.markdown(
f'''
In the past twenty years the DOW JONES INDUSTRIAL had these summary stats: 

minimum -**{DJImin}** 

maximum - **{DJImax}** 

median - **{DJImed}**

mean - **{DJImean}**

standard deviation - **{DJIstd}** 
'''

)

col3.header('DOW JONES')
col3.markdown('### Summary Statistics')
col3.markdown(
f'''
In the past twenty years the NASDAQ had these summary stats: 

minimum -**{IXmin}** 

maximum - **{IXmax}** 

median - **{IXmed}**

mean - **{IXmean}**

standard deviation - **{IXstd}** 
'''

)

st.write("From these summary statistics and our boxplot it's easy to see that there is a right skew amongst our data, with our medians being much further down than our max, and all 3 plots having relatively long tails in comparison to their boxes. This can be explained by the recent bullish behaviors of the stocks both post-COVID and post 2008 recession. ")
