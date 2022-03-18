# TrendListGenerator

Trendlist Generator is a couple of console applications tools that aims to generate fresh wordlists that can be used by **bruteforce** tools. It can be used to collect data from **Google Trends** thanks to the **pytrends** API and to deduce password lists from it.

## Pytrends
https://github.com/GeneralMills/pytrends  
https://pypi.org/project/pytrends/

### Install

pip install pytrends

### Requirement

Written for Python 3.3+

## Scraper.py

Is the first script of the **TrendListGenerator** Stack. Can be use to crawl trending key words with parametered queries through pytrends api. 

First input a country number from the query compatible coutries list: https://trends.google.com/trends/hottrends/visualize/internal/data shown on your terminal. Then input a query number and parameters if necessary to get the wordlist output. Finally you can save the list in a file.

> ### Queries
>
> - Trending Searches
> - Related Topics
> - Related Queries
> - Top Charts
> - Suggestions

## Mixer.py

The second script of the Stack. Can be used to apply rules on the crawled wordlist to extend the passwords patterns.

First you have to open a wordlist by typing its location from the project's directory. Then you have to choose a mode number and a rules numbers list to output the expanded wordlist.

> ### Modes
>
> - Unique list
> - Multiple lists
> - Every lists

> ### Rules
>
> - Inter word
> - Special chars
> - Lowercase
