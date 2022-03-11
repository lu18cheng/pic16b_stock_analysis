# Growth Stocks vs. Value Stocks :money_with_wings::money_with_wings::money_with_wings:
:fire: Team Name: Litquidity  
:rocket: Team Members: Lu Cheng, Samuel Shi  

Growth stock investing and value stock investing have been the most common strategies in equity investing, and the debate over their effectiveness has lasted for years. In this project, we study the past stock prices to compare the performance of growth stocks vs. value stocks over different periods and use machine learning models to examine the correlations between their performance and various macroeconomic factors such as interest rates, inflation rate, GDP growth rate, etc. In summary, we hope our project can provide more insights for the retail investors into which strategy is more effective for a given time horizon and under various economic conditions.


This repository includes all the code to the analysis. 
- `proposal.md` includes the initial project proposal.
- `economy_data` and `stock_data` folders include the stock prices data we found for the past 20 years from [Yahoo Finance](https://finance.yahoo.com/) and data for macroeconomic indicators for the past 50 years from [Federal Reserve's website](https://fred.stlouisfed.org/).
- `db` folder includes the database we built with the data.
- `code` folder includes all the code used in our analysis, including code to create database, pull and clean data from database, create visualizations and train various time series, machine learning & deep leanning models. 
- `Images` folder stores visualizations made in the project 
- `webapp` includes a flask web app to deploy our results and create an interactive page to help users predict potential stock price changes. 

