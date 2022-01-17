from pytrends.request import TrendReq

# Google connection
pytrends = TrendReq(hl='en-US', tz=360)

# Trending searches in real time for a specified country
def listTrends(country_name):
    print(pytrends.trending_searches(pn=country_name))
    
# Payload building with a keywords list or categories
def buildPayload(keywords_list):
    pytrends.build_payload(keywords_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    
# Mode Acquisition
mode_id = input(" Do you wish to search by : Trending Searches (real time) = 1, Related Topics (up to 5 keywords) = 2, Top Charts = 3 ?")

kw_list = ["audi"]

# Country Acquisition
country_id = input(" Enter a country number : France = 1, USA = 2, Japan = 3, Russia = 4 ")

# Country Restitution
print(" You choosed the number "+country_id)

if country_id == '1':
    country = 'france'
elif country_id == '2':
    country = 'united_states'
elif country_id == '3':
    country = 'japan'
else:
    country = 'russia'
    
print(" The country is set to "+country)
listTrends('US')

#print(pytrends.top_charts('2021', hl='en-US', tz=300, geo='GLOBAL'))
buildPayload(kw_list)
#print(pytrends.related_topics())
#print(pytrends.categories())

