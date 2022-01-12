from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

#Creation du payload
#kw_list = ["Football"]
#pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

print(pytrends.trending_searches(pn='france'))
