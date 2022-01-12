from pytrends.request import TrendReq

#Google connection
pytrends = TrendReq(hl='en-US', tz=360)

#Payload creation
#kw_list = ["Football"]
#pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

#Trending searches in real time for a specified country
print(pytrends.trending_searches(pn='france'))
print(pytrends.trending_searches(pn='united_states')) 
print(pytrends.trending_searches(pn='japan'))
print(pytrends.trending_searches(pn='russia'))