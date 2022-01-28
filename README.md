# Growth Stocks vs. Value Stocks :money_with_wings::money_with_wings::money_with_wings:
:fire: Team Name: Litquidity  
:rocket: Team Members: Lu Cheng, Samuel Shi  

## Abstract
Growth stock investing and value stock investing have been the most common strategies in equity investing, and the debate over their effectiveness has lasted for years. In this project, we will study the past stock prices to compare the performance of growth stocks vs. value stocks over different periods and use machine learning models to examine the correlations between their performance and various macroeconomic factors such as interest rates, inflation rate, GDP growth rate, etc. In summary, we hope our project can provide more insights for the retail investors into which strategy is more effective for a given time horizon and under various economic conditions.

## Planned Deliverables
An overall interactive website/blog that includes the following content:
- an informative webpage detailing methodologies, findings and our conclusion. *There can be multiple brilliant and complex graphs to demonstrate our results and the weighted stock prices*
- an interactive interface so that users can do various scenario analysis to adjust their portfolio accordingly. *For instance, there could be a toggle so the website user can choose the specific time horizon: '5 years' '10 years''20 years', or the economic conditions shift: "interest rate increases 0.25%", "GDP growth rate slows down by 0.5%", etc.* 

## Resources Required
- Stock prices for the past 50 years from [Yahoo Finance](https://finance.yahoo.com/)
- Macroeconomic indicators for the past 50 years from [Federal Reserve's website](https://fred.stlouisfed.org/)
- If the data is large, may also require cloud environment to store data & train machine learning model 

## Tools and Skills Required
- Basic knowledge on stocks and macroeconomics so we can devise a straightforward and scientific way to categorize the stocks into either the "growth bucket" or the "value bucket" 
- Database managment to store all the prices information
- Visualization skillsets to examine the changes in stock prices, or macroeconomic indicators
- Time series Machine learning models for stock analysis (maybe start with ARIMA in statsmodels package)
- Other machine learning models, depending on the eventual analysis, may use various types of regression model 

## What You Will Learn
- Version control with and collaboration on git 
    Each step of the project would be tracked using git and there would be a lot to learn abotu version controls and what to do if there is a conflict with pushing file changes 
- Database management
    Since the project would involve many large datasets (Stock prices and macroeconomic indicators for the past 50 years), we would be more familar with databse management at the end of the project 
- Web development and report/blog writing 
- Data Visualizations
    Practices with multiple types of visualizations would be involved in this project, especially how to make interactive interface for users to do scenario analysis 
- Machine Learning Modeling
    We would learn about time series machine learning models for this project as well as the the skills to find the most optimal model for our objectives
- Project management 

## Risks
There are two things that could potentially stop us from achieving the full deliverable:
1. We have the inherent assumption that growth stock investing vs. value stock investing are two distinct investing methodologies that will yield different investment returns. It is possible that such categorization is only a human invention and under certian circumstances, there are no material differences between the two strategies. **However, based on empirical evidence, the two categories do yield different results for different time period. We can provide a literary review to provide some academic support to such categoriztion.**
2. We have the inherent assumption that macroeconomic factors do have different impacts on the performances of the two stocks. It may turn out that the real world and the real economy is much more complicated and the study on the correlation between the economic indicators (that are subject to our choice) and stock performance will not yield meanningful results. Then our conclusion maybe limited to provide investment guidance for the retail investors. **However, we can try to employ more economic indicators and models to study the coorelation and prevent overfitting.**

## Ethics
The input data mostly consists of past stock prices, economic indicators, and calculated market indices, which are less prone to the risks of bias. As this data is readily available to all investors with Internet access, the project only aims to add an extra layer of information to help individual investors make more educated decisions in the financial market. 
> Group of people that will likely benefit from this project: retail investors, institutional investors, policy makers, etc.

However, most of the time, the public investing space is a zero-sum game. So,
> Some individuals and their trading strategies might have already incorporated the patterns and correlations, and the disclosure of such analysis will potentially harm their gains. 

But overall, we believe in the following assumptions why the project can make the world a better place:
1. More information and statistical analysis will provide more transparency and better decision mechanism to retail investors. We assume investment returns and financial gains are important to them. Arguably, financial freedom is one of the most crucial indicator of happiness. 
2. The findings and conclusions of this project can potentially contribute to the better understanding of how the market works. A study on the correlation with various economic factors can facilitate policy makers to better maintain the efficieny of the market. We assume the efficiency of the economy can make the world a better place because "good products and services" will be allocated with the best resources. 
 
## Tentative Timeline
- In 2 weeks: data collection and cleaning
    - [ ] establish a database containing all the stock prices and relevant information (valuation multiple, economic indicators, etc.)
    - [ ] find a relevant criteria to categorize the stocks (is P/E multiple the best?)
- In 4 weeks: organize insights from model and start writing report 
    - [ ] choose appropriate machine learning models to train the dataset
    - [ ] study the ouput of the models and generate insights
- In 6 weeks: finalize the report and clean up code 
    - [ ] run additional models if necessary
    - [ ] create visualizations to help our presentation and add insights to the conclusion
    - [ ] upload our findings and tools to the website
    - [ ] reflect what can be improved for the project

