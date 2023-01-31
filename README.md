# APRA (AMAZON PRODUCT REVIEW ANALYSIS) DESCRIPTIONS [![Build Status](https://app.travis-ci.com/chen-yuhong/DATA533-step3.svg?branch=main)](https://app.travis-ci.com/chen-yuhong/DATA533-step3)
### Amazon Product Review Analysis
The purpose of this review analysis application is to retrieve and display up to 10 keywords in one-star reviews, using the APIs provided by www.asindataapi.com Throughout this application, you’ll see that we’ve created API calls and classes to retrieve lists of the top 10 most helpful one-star reviews (which you can use to filter for specific amazon domain) and the top 10 most representative negative adjectives. 

The premise of this package is that the Amazon seller has a product with high sales volume and receives a lot of reviews. However, due to different batches, defects in products may not be found in time, which will lead to an increase in the number of bad reviews and a decrease in sales. But the Amazon seller may not know it because the factory may have changed some of its production patterns. Our goal is for Amazon sellers to use keywords in bad reviews to increase sales of their products. For example, one Amazon seller was selling a kitchen faucet that was selling well and had a lot of positive reviews. But in a short period of time, there were a lot of bad reviews, and through the analysis of the keyword bad reviews, there were a lot of water nozzle problems. After a discussion with the factory, it was found that the factory arbitrarily changed the design of the nozzle, which caused the defect. It is time consuming to read a lot of bad reviews and summarize them, so our package can save Amazon sellers a lot of time to summarize bad reviews. Is that why we only care about bad reviews and not good reviews.


Register an account: https://app.asindataapi.com/signup

Check out the API documentation:https://www.asindataapi.com/docs

### usage steps
1. The first step is to create your API Key (https://app.asindataapi.com/signup). 
Please notice that the free account only has 100 free requests trials
  
2. Run ```play.py``` file

![alt text](https://github.com/chen-yuhong/data534project/blob/yuhong/screenshots/step1.png)

3. Select Amazon Domain from the menu bar (US, Canada, UK, Australia)
4. Enter API Key
5. Enter product ASIN number (Each product on amazon has own unique ASIN number)
6. Click ```Submit``` button




### apra
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|return_url()| return url based on user's input of api key, amazon domain and asin number|
|clean_content()| clean content of labels every time run the program|
|get_review()|get the content, count and percentage of one-star review from the url request. And raise exceptions whenever there is Api key error, asin number error, amazon domain error|
|clean_text()|remove special characters and numbers in bad reviews|
|negative_words()|use SentimentIntensityAnalyzer() to get negative words from bad reviews and sort by the word that appears most frequently|
|output_result()|function for clicking the button and output results|

