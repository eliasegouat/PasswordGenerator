from pytrends.request import TrendReq

# Google Connection
pytrends = TrendReq(hl='en-US', tz=360, retries=2, timeout=(10,25))

# Country Selection
def selectCountry():
    country_list = [['argentina','AR'],['australia','AU'],['austria','AT'],['belgium','BE'],
                    ['brazil','BR'],['canada','CA'],['chile','CL'],['colombia','CO'],
                    ['czech_republic','CZ'],['denmark','DK'],['egypt','EG'],['finland','FI'],
                    ['france','FR'],['germany','DE'],['greece','GR'],['hong_kong','HK'],
                    ['hungary','HU'],['india','IN'],['indonesia','ID'],['ireland','IE'],
                    ['israel','IL'],['italy','IT'],['japan','JP'],['kenya','KE'],
                    ['malaysia','MY'],['mexico','MX'],['netherlands','NL'],['new zealand','NZ'],
                    ['nigeria','NG'],['norway','NO'],['philippines','PH'],['poland','PL'],
                    ['portugal','PT'],['romania','RO'],['russia','RU'],['saudi_arabia','SA'],
                    ['singapore','SG'],['south_africa','ZA'],['south_korea','KR'],
                    ['sweden','SE'],['switzerland','CH'],['taiwan','TW'],
                    ['thailand','TH'],['turkey','TR'],['ukraine','UA'],['united_kingdom','GB'],
                    ['united_states','US'],['vietnam','VN']]

    output_str = "Select a country : \n"
    for country in country_list :
        output_str += '    '+str(country_list.index(country))+'. '+country[0]+'\n'
    output_str+= "Enter the country number : "
    country_id = input(output_str)
    return country_list[int(country_id)]

# Trending Searches Query Selection
def selectTrendingSearches():
    country = selectCountry()
    query = pytrends.trending_searches(pn=country[0])
    result = query[0].tolist()
    return result

# Related Topics Query Selection
def selectRelatedTopics():
    country = selectCountry()
    kw_list = input("Enter a keyword : ").split()
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo=country[1], gprop='')
    query = pytrends.related_topics()
    top = query[kw_list[0]]['top']['topic_title'].tolist()
    rising = query[kw_list[0]]['rising']['topic_title'].tolist()
    top.extend(rising)
    result = list(set(top))
    return result

# Related Queries Query Selection
def selectRelatedQueries():
    country = selectCountry()
    kw_list = input("Enter a keyword : ").split()
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo=country[1], gprop='')
    query = pytrends.related_queries()
    top = query[kw_list[0]]['top']['query'].tolist()
    rising = query[kw_list[0]]['rising']['query'].tolist()
    top.extend(rising)
    result = list(set(top))
    return result

# Top Charts Query Selection
def selectTopCharts():
    country = selectCountry()
    year = input("""Year(YYYY) post 2010 excluding the current : """)
    query = pytrends.top_charts(year, hl='en-US', tz=300, geo=country[1])
    result = query['title'].tolist()
    return result

# Suggestions Query Selection
def selectSuggestions():
    keyword = input("Enter suggestion keyword : ")
    suggestions = list()
    query=pytrends.suggestions(keyword)
    for suggestion in query :
        suggestions.append(suggestion['title'])
        suggestions.append(suggestion['type'])
    result = list(set(suggestions))
    return result
    
# Query Selection
def selectQuery():
    query_id = input("""Select a query :
    1. Trending Searches (real time, 20 values)
    2. Related Topics (keyword related)
    3. Related Queries (keyword related)
    4. Top Charts
    5. Suggestions (keyword related)
    Enter the query number : """)
    
    if query_id == '1':
        result = selectTrendingSearches()
    elif query_id == '2':
        result = selectRelatedTopics()
    elif query_id == '3':
        result = selectRelatedQueries()
    elif query_id == '4':
        result = selectTopCharts()
    elif query_id == '4':
        result = selectSuggestions()
    else :
        print("Select a valid query number")
        result = selectQuery()
    return result

# Wordlist Writting to a file
def toFile(wordlist):
    response = input("Save the wordlist in a text file ? (yes|no) : ")
    if response == 'yes' or response == 'y':
        file_name = input("Enter a filename : ")
        with open(file_name+'.txt', mode='w', encoding='utf-8') as f:
            for word in wordlist:
                f.write(word)
                f.write('\n')

res = selectQuery()
print(res)
toFile(res)