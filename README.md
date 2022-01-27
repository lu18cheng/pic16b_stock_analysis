# pic16b_stock_analysis
Team Members: Lu Cheng, Samuel Shi

## Abstract
Growth stock investing and value stock investing have been the most common strategies in equity investing, and the debate over their effectiveness has lasted for years. In this project, we will study the past stock data to compare the performance of growth stock vs. value stocks over different periods and use machine learning models to examine their correlations with various macroeconomic factors such as interest rates, inflation rate, GDP growth rate, etc. In summary, we hope our project can provide more insights for the retail investors into which strategy is more effective for a given time horizon and under various economic conditions.

## Planned Deliverables
An overall interactive website/blog that includes the following content:
- an informative webpage detailing methodologies, findings and our conclusion. They can be multiple brilliant and complex graphs to demonstrate our results and the weighted stock prices
- an interactive interface so that users can do various scenario analysis to adjust their portfolio accordingly. For instance, there could be a toggle so the website user can choose the specific time horizon: '5 years' '10 years''20 years', or the economic conditions shift: "interest rate increases 0.25%", "GDP growth rate slows down by 0.5%", etc. In short, it will be an interactive model so that users can do various scenario analysis to adjust their portfolio. 

## Resources Required
- Stock prices for the past 50 years from [Yahoo Finance](https://finance.yahoo.com/)
- Macroeconomic indicators for the past 50 years from [Federal Reserve's website](https://fred.stlouisfed.org/)
- If the data is large, may also require cloud environment to store data & train machine learning model 

## Tools and Skills Required
- Basic knowledge on stocks and macroeconomics so we can devise a straightforward and scientific way to categorize the stocks into either the "growth bucket" or the "value bucket" 
- Database managment to store all the prices information
- Visualization skillsets to examine the changes in stock prices, or macroeconomic indicators
- Time series Machine learning models (maybe start with ARIMA in statsmodels package)
- some other machine learning models ???

## What You Will Learn
- Version control with git 
- Time series machine learning models 
- Project management 

## Risks
There are two things that could potentially stop us from achieving the full deliverable:
1. we have the inherent assumption that growth stock investing vs. value stock investing are two distinct investing methodologies that will yield different investment returns. It is possible that such categorization is only a human invention and under certian circumstances, there are no material differences between the two strategies. **However, based on empirical evidence, the two categories do yield different results for different time period. We can provide a literary review to provide some academic support to such categoriztion.**
2. we have the inherent assumption that macroeconomic factors do have different impacts on the performances of the two stocks. It may turn out that the real world and the real economy is much more complicated and the study on the correlation between the economic indicators (that are subject to our choice) and stock performance will not yield meanningful results. Then our conclusion maybe limited to provide investment guidance for the retail investors. **However, we can try to employ more economic indicators and models to study the coorelation and prevent overfitting.**

## Ethics
...
 

## Tentative Timeline
- In 2 weeks: obtain data and train a preliminary model
- In 4 weeks: organize insights from model and start writing report 
- In 6 weeks: finalize the report and clean up code 
