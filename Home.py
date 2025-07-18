import streamlit as st
import matplotlib.pyplot as plt
import joblib

st.set_page_config(initial_sidebar_state="expanded")
st.set_page_config(page_title = 'Home')
st.title('Welcome To My Portfolio')

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

Hello Everyone, my name is Eduard Klyuchinskiy and this is my attempt at creating a public show case for my projects.
Currently, the only project I feel comfortable sharing is my stock forecasting project that I began developing for
my data science Master's degree capstone. I am currently still working on this project, and I will continue to update
it as time progresses. 
In the sidebar you can find links to my resume and any projects I feel comfortable sharing with you. 

## About Me

I have completed my final semester of my Master's program and have thoroughly enjoying learning all about data science,
especially the machine learning portion of the course. Throughout my time in the program I've learned so much about
both the math side of data science and programming side of data science, to the point where I think I have a solid understanding of how 
websites and programs work behind the scenes. 

My job in the U.S. Air Force is also very much related to data. In the Air Force I act more as a data analyst, and conduct actions most people would expect a data analyst do with data sets
such as cleaning it, processing it, and extracting insights out of it. I've taken a lot of what I've learned from my Master's and have been able to
apply it to my job. For example, I was able to build a SQL database using microsoft access and link that database to PowerBI
and sharepoint in order to streamline a lot of the manual processes that existed in my workplace beforehand. 
Additionally, I also have a Bachelor's in Management Information Systems, this initial education milestone propelled my desire to learn more about what makes computers and software work.
I take what I learned about the strategic and tactical methodologies related to managing information systems and apply them to my work ethic as well as what you may see in the projects that
are in the sidebar.

In my freetime(the little of it that I have) I am a huge videogame nerd, but who isn't these days? I also love going on hikes
running, and traveling. I'm originally from New York and I intend to go back after completing my service with the military. 
I'm hoping that during my transition I'll be able to utilize projects such as this as well as my resume and skills I've developed
to find myself a potential career that I can thrive in.

## About the Stock Price Forecasting Project

I wanted to make a project that would encourage people to invest into the economy over a long term period of time (like 10 years)
In order to do so, my idea was to create a project that forecasts the price of index funds 10 years int othe future and return
a CAGR (Compound Annual Growth Rate). What sets aside my forecasting project from many other ones you'll see online is that the other forecasters online
act more like a calculator where you plug in a number, a percentage rate, and it will give you a return in the end, my project
used a Deep Learning model called 'Long Short Term Memory' to train over 20 years of stock data. It will predict a new price for an index fund every day
for the next 10 years and as a result, will produce its own CAGR utilizing the historical data it was trained on.
With this in mind, the Long Short Term 
Memory by its design gives a larger weight to more recent data. This weight it attributes to more recent data is why I picked this model, so that in the forecast function the model can 
pick up where it left off from training the past 20 years, and be utilized as a forecaster making predictions for the next 10 years. 
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

col3.header('NASDAQ')
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

st.write("From these summary statistics and our boxplot it's easy to see that there is a right skew amongst our data, because our medians being much further down than our max, and all 3 plots having relatively long tails in comparison to their boxes. This can be explained by the recent bullish behaviors of the market post covid which created prices that trend much higher than the majority of the data beforehand.")
