from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Football"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

print(pytrends.related_topics())
print(pytrends.related_queries())