from pytrends.request import TrendReq

# Google connection
pytrends = TrendReq(hl='en-US', tz=360, retries=2, timeout=(10,25))

# Selection of a specific country for search
def chooseCountry():
    # Country definition
    global country, geopos
    
    # Country Acquisition
    country_id = input("""Countries :
    1. France
    2. USA
    3. Japan
    4. Russia
    5. Global
    Enter a country number : """)

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
    
# Selection of a specific mode for each query
def chooseMode():
    # Mode Acquisition
    mode_id = input("""Search Modes :
    1. Trending Searches (real time)
    2. Related Topics (up to 5 keywords)
    3. Related Queries (up to 5 keywords)
    4. Top Charts
    5. Suggestions (related to a keyword)
    Enter a mode number : """)
    
    if mode_id == '1':
        chooseCountry()
        print(pytrends.trending_searches(pn=country))
    elif mode_id == '2' or mode_id == '3':
        chooseCountry()
        global geopos
        if geopos == 'GLOBAL':
            geopos = ''
        kw_list = input("Enter up to 5 topics (separated by space) for search ").split()
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo=geopos, gprop='')
        if mode_id == '2':
            print(pytrends.related_topics())
        else :
            print(pytrends.related_queries())
    elif mode_id == '4':
        chooseCountry()
        year = input("Choose a specific year after 2010, excluding the current one (format => YYYY) ")
        print(pytrends.top_charts(year, hl='en-US', tz=300, geo=geopos))
    else :
        keyword = input("Enter the keyword to get suggestions for ")
        print(pytrends.suggestions(keyword))

#chooseMode()

#print(pytrends.suggestions('football'))

#print(pytrends.categories())

