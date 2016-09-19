# add libraries 
import pandas
import wikipedia


# import urllib.request
#url = r"https://d.docs.live.net/22403da9fb53b299/Pubic/BigDataRoadmap.xlsx"
#request = urllib.request.Request(url)
#response = urllib.request.urlopen(request)
#BigDataRoadmap = pandas.read_excel(response)


# import xls
BigDataRoadmap = pandas.read_excel("C:/Users/Rich/Documents/RandomData/BigDataRoadmap.xlsx")



# extract topic column
Topic = BigDataRoadmap.Topic

# init counter
i = 0

# pre allocate lists
searchItems = []
summaryItems = []


# loop through topics
for T in Topic:
    # increment counter
    i += 1

    # disp current iteration
    print(i," of ",len(Topic),": ", T)
    
    # perform and append search result
    try:
        searchItems.append(wikipedia.search(T))
    except :
        searchItems.append([])
    
    # perform and append summary result
    try:
        summaryItems.append(wikipedia.summary(T))
    except :
        summaryItems.append([])


    