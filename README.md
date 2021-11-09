# Welcome to my playground!
This is my personal playground for learning more about AI and testing different approaches to implement ML in 
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
### What learning algorithm to use?
#### Q-Learning
I started with this approach because it was used in the [example](https://www.gocoder.one/blog/rl-tutorial-with-openai-gym)
I used to orientate myself on. But I will look further for more suiting learning algorithms.
#### Linear regression
For my use-case many people on the internet are convinced that this is the best one to 
predict a stock price. Anyways I will stay with the Q-Learning, add some time awareness and
try my luck.

Update: Well that was a stupid idea, because the Q-Learning has its state list and only learns
from what action brings (or not brings) from this particular state, so unless the bitcoin price
has reoccurring patterns, this won't do much good, but for learning purposes I will still continue.

Up-Update: My prediction algorithm learned that 0 is more efficient than most of the other predictions
therefore if Bitcoin is at 0$ next week I predicted it, in any other case my attempt failed.