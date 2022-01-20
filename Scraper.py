from pytrends.request import TrendReq

# Google connection
pytrends = TrendReq(hl='en-US', tz=360)

# Trending searches in real time for a specified country
def listTrends(country_name):
    print(pytrends.trending_searches(pn=country_name))
    
# Payload building with a keywords list or categories
def buildPayload(keywords_list, geoposition):
    pytrends.build_payload(keywords_list, cat=0, timeframe='today 5-y', geo=geoposition, gprop='')

# Selection of a specific country for search
def chooseCountry():
    # Country definition
    global country
    
    # Country Acquisition
    country_id = input(" Enter a country number : France = 1, USA = 2, Japan = 3, Russia = 4, Global = other")

    # Country Restitution
    print(" You choosed the number "+country_id)

    if country_id == '1':
        country = 'france'
        geopos = 'FR'
    elif country_id == '2':
        country = 'united_states'
        geopos = 'US'
    elif country_id == '3':
        country = 'japan'
        geopos = 'JP'
    elif country_id == '4':
        country = 'russia'
        geopos  = 'RU'
    else :
        country = 'united_states'
        geopos = 'GLOBAL'
    
    print(" The country is set to "+country)
    
# Mode Acquisition
mode_id = input(" Do you wish to search by : Trending Searches (real time) = 1, Related Topics (up to 5 keywords) = 2, Top Charts = 3 ?")

kw_list = ["audi"]

chooseCountry()

print(" The country is set to "+country)
listTrends(country)

#print(pytrends.top_charts('2021', hl='en-US', tz=300, geo='GLOBAL'))
buildPayload(kw_list, '')
print(pytrends.related_topics())
#print(pytrends.categories())

