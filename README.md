# Welcome to my playground!
This is my personal playground for learning more about AI and testing different approaches to implement RL in 
my day-to-day life.
## 01 - Crypto predictions
My first goal is to see how the openAI gym works and try to make the program learn from 
crypto-market data to predict future developments.
### Do you have any more of this data?
Probably one of the most important question in machine learning, where do I get my training data from?\
I found some sources, for example [here](https://pro.coinmarketcap.com/contact-data/), for a small loan of a million dollars
you can get anything, but I am not Trump, so I decided to get the data myself [at this link](https://coinmarketcap.com/historical/)
.\
So far so good, but I remembered I am lazy, so I am not going to click through all those websites and get the data and
write it all in a file like a worker bee. No I am going to make a [webcrawler](https://scrapy.org/) who does the work for me.