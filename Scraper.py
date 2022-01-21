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
    
# Query Selection
def selectQuery(country):

    query_id = input("""Select a query :
    1. Trending Searches (real time, 20 values)
    2. Related Topics (Up to 5 keywords)
    3. Related Queries (up to 5 keywords)
    4. Top Charts
    5. Suggestions (related to a keyword)
    Enter the query number : """)
    
    if query_id == '1':
        query = pytrends.trending_searches(pn=country[0])
        result = query[0].tolist()
    elif query_id == '2':
        kw_list = input("Enter up to 5 topics (separated by space) for search : ").split()
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo=country[1], gprop='')
        query = pytrends.related_topics()
        top = query[kw_list[0]]['top']['topic_title'].tolist()
        rising = query[kw_list[0]]['rising']['topic_title'].tolist()
        top.extend(rising)
        result = list(set(top))
    elif query_id == '3':
        kw_list = input("Enter up to 5 topics (separated by space) for search : ").split()
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo=country[1], gprop='')
        result = pytrends.related_queries()
    elif query_id == '4':
        year = input("""Choose a specific year after 2010,
                        excluding the current one (format => YYYY) : """)
        result = pytrends.top_charts(year, hl='en-US', tz=300, geo=country[1])
    else :
        keyword = input("Enter a keyword : ")
        print(pytrends.suggestions(keyword))
    return result

country = selectCountry()
res = selectQuery(country)
print(res)

