from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

#Payload creation
#kw_list = ["Football"]
#pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

print(pytrends.trending_searches(pn='france'))# trending searches in real time for France
print(pytrends.trending_searches(pn='united_states')) 
print(pytrends.trending_searches(pn='japan'))
print(pytrends.trending_searches(pn='russia'))