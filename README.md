# TrendListGenerator

Trendlist Generator is a couple of scripts tools that aims to generate fresh wordlists that can be used by **bruteforce** tools. It can be used to collect data from **Google Trends** thanks to the **pytrends** API and to deduce password lists from it.

## Pytrends
https://github.com/GeneralMills/pytrends  
https://pypi.org/project/pytrends/

### Install

pip install pytrends

### Requirement

Written for Python 3.3+

## Scraper.py

Is the first script of the **TrendListGenerator** Stack. 

> ### Queries
>
> - Trending Searches
> - Related Topics
> - Related Queries
> - Top Charts
> - Suggestions

## Mixer.py

The second script of the Stack.

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
