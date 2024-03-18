import requests
from bs4 import BeautifulSoup
import time


def scrape_twitter_account(account, symbol):
    mentions_count = 0
    response = requests.get(account)
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets = soup.find_all('div', {'data-testid': 'tweet'})
    for tweet in tweets:
        tweet_text = tweet.find('div', {'class': 'tweet-text'}).text
        if symbol.lower() in tweet_text.lower():
            mentions_count += 1
    return mentions_count


def scrape_twitter_accounts(accounts, symbol):
    total_mentions_count = 0
    for account in accounts:
        mentions = scrape_twitter_account(account, symbol)
        print(f"{symbol} was mentioned {mentions} times in {account}.")
        total_mentions_count += mentions
    return total_mentions_count


# List of Twitter accounts to scrape
twitter_accounts = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox'
]

# Ticker symbol to search for
ticker_symbol = '$TSLA'

# Time interval for scraping session (in minutes)
scraping_interval=int(input("Enter Number of minutes: "))


while True:
    total_mentions = scrape_twitter_accounts(twitter_accounts, ticker_symbol)
    print(f"Total mentions of {ticker_symbol}: {total_mentions} times in the last {scraping_interval} minutes.")
    time.sleep(scraping_interval * 60)  # Convert minutes to seconds
