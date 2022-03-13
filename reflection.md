# Project Reflections
## Growth Stocks vs. Value Stocks :money_with_wings::money_with_wings::money_with_wings:
:fire: Team Name: Litquidity  
:rocket: Team Members: Lu Cheng, Samuel Shi  

## Overall, what did you achieve in your project? 
Our project aims to answer two questions:
- How has the performances of growth stocks and value stocks changed over the years?
- Are there any correlations between economic factors (such as inflation, exchange rate, and 10 year Treasury yield) and the performances of the stocks? If there's any correlation, how will growth stocks and value stocks respond respectively?

We employed Time Series Modeling (TSM), in particular SARIMAX and ARIMA, to answer the first question. Based on our data (20 years of daily stock data), growth stocks can be forecasted with much better accuracy than value stocks. To answer the second question, we have employed a plethora of regression models to study the correlations and produce the results in the following table:

{include an image here}

Since our neural network models have consistently produced mininal Mean Squared Error (MSE) with little evidence of overfitting for both value and growth stocks, we chose to embed them into our webapp for the users to experiment with. 

In the last step, we managed to build a webapp that delivered two functions:
1. a detailed summary of our assumptions and conclusions. In particular, an explanation of where we find the data of our project, how we construct the models to analyze the correlations, what our results are telling about the correlations, and some limitations why our models may not yield desirable results;
2. an interactive app to tell the users what are some predicted changes to the stock price according to our model. Specifically, users can choose to analyze a value/growth stock, then input the percentage changes of inflation rate, exchange rate against Canadian dollars, and 10 Year Treausry yield, and the program will return a predicted change of the stock price. An example has been included as follows, and we can compare how value and growth stocks can respond to certain macroeconomic changes:

{include an image here}

## What are two aspects of your project that you are especially proud of? 

## What are two things you would suggest doing to further improve your project?
There are mainly two areas that we can potentially improve our project: **data collection** and **modeling**.
- **data collection**: Although we have spent quite amount of time discussing how to and what kind of data to be included in our model, we still feel it is inadequate. Due to time constraint, we chose IVE and IVW as two indices to represent the overall performances of growth stocks and value stocks. One drawback is that both of these indices were created in 2003, which gives us *only around 20 years of data*. In reality, the debate between growth stocks and value stocks dated even before the Great Depression in the 1930s. A more scientific way is to find certain metrics to individually select stocks to construct a portofolio for growth stocks and value stocks respectively since 1930 instead of using generic metrics that only have spanned 20 years. 
- **modeling**: By trial and error, we probably can find better models that fit our purposes. For instance, SARIMAX and ARIMA might not be the best models for stock markets. Different TSM might be used for short term vs. long term predictions. Additionally, with some literature review, we can potentially find some models tackling similar problems. We can use transfer learning and other methods to improve our accuracy. 

## How does what you achieved compare to what you set out to do in your proposal? 
- We pretty much followed the timeline and goals set in our intial proposal. However, we won't able to obtain an accurate enough model to help us predict the market and provide meaningful insights about how the market responds to changes in macroeconomic indicators. 

## What are three things you learned from the experience of completing your project? Data analysis techniques? Python packages? Git + GitHub? Etc? 
- We learned many useful skills through this project, from project management, communication and presentation skills, to version control (github), data base management, data visualization,  machine learning modeling and webdesign

## How will your experience completing this project will help you in your future studies or career? Please be as specific as possible. 
- This experience is helpful to help us prepare for a data science career as it mimics the process of a complete data science project in a real life experience. In actual working setting, we imagine most projects would go through the process of proposal -> data collection & cleaning -> actual analysis -> presentation of results. Version control with git is also a crucial tool in working setting. Moreover, many of the difficulties we encounter in this project could be similar to what we may encounter in real life. Being able to detect where the issues come from and exploring ways to solve it is a useful skill to have when working on industry projects. 
