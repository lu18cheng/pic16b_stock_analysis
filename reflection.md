# Project Reflection by Team Litquidity  
## Growth Stocks vs. Value Stocks :money_with_wings::money_with_wings::money_with_wings:
:fire: Team Name: Litquidity  
:rocket: Team Members: Lu Cheng, Samuel Shi  
*(We work on the first 5 parts collectively and part VI individually)*

## I. Overall, what did you achieve in your project? 
Our project aims to answer two questions:
- How has the performances of growth stocks and value stocks changed over the years?
- Are there any correlations between economic factors (such as inflation, exchange rate, and 10 year Treasury yield) and the performances of the stocks? If there's any correlation, how will growth stocks and value stocks respond respectively?

We employed Time Series Modeling (TSM), in particular SARIMAX and ARIMA, to answer the first question. Based on our data (20 years of daily stock data), growth stocks can be forecasted with much better accuracy than value stocks. To answer the second question, we have employed a plethora of regression models to study the correlations and produce the results in the following table:

{include an image here}

Since our neural network models have consistently produced mininal Mean Squared Error (MSE) with little evidence of overfitting for both value and growth stocks, we chose to embed them into our webapp for the users to experiment with. 

In the last step, we managed to build a webapp that serves two functions:
1. a detailed summary of our assumptions and conclusions. In particular, an explanation of where we find the data of our project, how we construct the models to analyze the correlations, what our results are telling about the correlations, and some limitations why our models may not yield desirable results;
2. an interactive app to tell the users what are some predicted changes to the stock price according to our model. Specifically, users can choose to analyze a value/growth stock, then input the percentage changes of inflation rate, exchange rate against Canadian dollars, and 10 Year Treausry yield, and the program will return a predicted change of the stock price. An example has been included as follows, and we can compare how value and growth stocks can respond to certain macroeconomic changes:

{include an image here}

<br>

## II. What are two aspects of your project that you are especially proud of? 
- **We managed to utilize data science techniques to develop better understanding of the stock market**: Most of our previous experiences with stock market and investing are qualitative. By finishing this project, we have become more aware of, for stock market analysis, where to collect data, how to process data cleaning, and what are some specific data sciences techniques that are available for such issues. In particular, it confirms our belief that modeling stock markets is indeed challenging. Moreover, it provides a new angle of investing into the secondary markets, and tells us what are some advantages and drawbacks of using data science and machine learning techniques to study the stock market. 
- **We built an interactive webapp that might impact a user's decision in real life**: we regard a piece of information to be "valuable" if it contributes to an individual's decision in real life, directly or indirectly. The webapp can help retail investors to better understand market dynamics and stock returns with acceptable margins of error *(0.8% for value stocks and 1% for growth stocks)*. Although it can hardly provide direct buy or sell suggestions, it offers a scientific way to examine the impacts of various macroeconomic factors on stock performances. Retail investors or other potential users can develop a better understanding of the correlations and make more informed decisions. 

<br>

## III. What are two things you would suggest doing to further improve your project?
There are mainly two areas that we can potentially improve our project: **data collection** and **modeling**.
- **data collection**: Although we have spent quite amount of time discussing how to and what kind of data to be included in our model, we still feel it is inadequate. Due to time constraint, we chose IVE and IVW as two indices to represent the overall performances of growth stocks and value stocks. One drawback is that both of these indices were created in 2003, which gives us *only around 20 years of data*. In reality, the debate between growth stocks and value stocks dated even before the Great Depression in the 1930s. A more scientific way is to find certain metrics to individually select stocks to construct a portofolio for growth stocks and value stocks respectively since 1930 instead of using generic metrics that only have spanned 20 years. 
- **modeling**: By trial and error, we can probably find better models that fit our purposes. For instance, SARIMAX and ARIMA might not be the best models for stock markets. Different TSM might be used for short term vs. long term predictions. Additionally, with some literature review, we can potentially find some models tackling similar problems. We can use transfer learning and other methods to improve our accuracy. 

<br>

## IV. How does what you achieved compare to what you set out to do in your proposal? 
In our project proposal, we proposed to study the performance of growth stocks vs. value stocks over different periods and use machine learning models to examine the correlations between their performance and various macroeconomic factors such as interest rates, inflation rate, etc. We are able to use time series models to model the trend of growth stock and value stock, and we built several machine learning models to predict stock performance with macroeconomic indicators as proposed. However, we aren't able to achieve high prediction accuracy with our model and thus can only have limited insights about how the market performs for a given time horizon and responds to changes in macroeconomic indicators. 
We also planned two deliverables in our project proposal.
1. an informative webpage detailing methodologies, findings and our conclusion. 
2. an interactive interface so that users can do various scenario analysis to adjust their portfolio accordingly. 
We have included those in our presentation, but due to time constriants, we have not managed to include a full report with methodologies, findings, and conclusions into a webpage. For number 2, though we made a rough interactive webapp that allows for user input for macroeconomic factors and displays predicted change in stock prices. Yet, due to the limits in our data, we are not able to develop a way for users to conduct scenario analysis.
Overall, we still think we did pretty well in terms of following the timeline achieving our goals for the project. 

<br>

## V. What are three things you learned from the experience of completing your project? Data analysis techniques? Python packages? Git + GitHub? Etc? 
<!--- We learned many useful skills through this project, from project management, communication and presentation skills, to version control (github), data base management, data visualization,  machine learning modeling and webdesign-->
- **Version control with and collaboration on git** Each step of the project is tracked using git. We experienced different types of conflicts throughout the project and learned ways to evetually resolve the conflict. 
- **Web development** We collarborately built an interactive web app to tell the users what are some predicted changes to the stock price according to our model. The process involves learning how to save, restore and feed user input to machine learning models, as well as html, css etc. 
- **Machine Learning & Time Series Modeling** We built several time series, machine learning and deep learning models in the project. We learned about the concepts behind the machine learning models and ways to tune the parameters to train a better model. 

<br>

## VI. How will your experience completing this project will help you in your future studies or career? Please be as specific as possible. 
- For Lu: This experience is helpful to help us prepare for a data science career as it mimics the process of a complete data science project in a real life experience. In actual working setting, we imagine most projects would go through the process of proposal -> data collection & cleaning -> actual analysis -> presentation of results. Version control with git is also a crucial tool in working setting. Moreover, many of the difficulties we encounter in this project could be similar to what we may encounter in real life. Being able to detect where the issues come from and exploring ways to solve it is a useful skill to have when working on industry projects. 
- For Samuel: Frankly speaking, much of the experiences will not be relevant with my career path at least in a short term, since I will be mainly working on primary market investing upon graduation. Nevertheless, the project has not only reshaped my understanding of data science methodologies, but also teaches me the intricacies of data preparation, analysis, and evaluation. It allows me to develop a more holistic view of how data science and machine learning can be applied in real life scenarios and what current trends, opportunities, controversies and obstacles are in these fields. As I am always intrigued by the interactions among business, technology, and societies, these experiences will contribute a small but pivotal piece to my overall mental framework. Therefore, the project will certainly fit my long term goal of understanding what "value" means for different stakeholders and how to create sustainable "values" for teams, organizations, and companies. 
