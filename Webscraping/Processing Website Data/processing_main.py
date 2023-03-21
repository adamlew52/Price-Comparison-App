import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
import tldextract as tld
import requests

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# start google search process
def Search(query, resultsNum, resultsStop):
    SearchResults = []
    for index, i in enumerate(search(query, tld= "com",num=resultsNum, stop=resultsStop, pause = 2)):
        #print(f"Resource: {i}")
        SearchResults.append(i)
    return SearchResults

def GoogleProduct(product, useCase):
    searchCrit = product
    searchCrit += useCase
    print(searchCrit)

    print(f'finding resources on {product}...')
    resultsNum = 20
    resultsStop = 20
    sourceList = Search(searchCrit,resultsNum, resultsStop)
    #print(f'The following resources were found for {product}:\n{sourceList}')
    #print(type(sourceList))
    return sourceList
# end google search process

def FindPrice(URL):
    #print(wb.open(str(URL)))

    htmlText = requests.get(URL).text #200 is the convention number stating it is connected
    soup = bs(htmlText, 'lxml')
    htmlElement = ""
    keyword = ""
    product  = soup.find_all(htmlElement, class_= keyword)

    try: 
        htmlElement = "span"
        keyword = "money"
        product  = soup.find_all(htmlElement, class_= keyword)
        return product
    except:
        print("failed to find the element and keyword combination successfully...")
        pass

#-------------------------------------------------------------------------------------------------
def GetPrice(searchResults, htmlElement, keyword):
    char = "$"
    htmlText = searchResults #200 is the convention number stating it is connected
    soup = bs(htmlText, 'lxml')
    jobs = soup.find_all(str(htmlElement), class_= str(keyword))
    failCounter = 0

    for index, job in enumerate(jobs):
        #publishedDate = job.find(htmlElement, class_= keyword).text #search first
        #print(f"publishedDate variable (should actually be the price): {publishedDate}")
        print(f"job: \t{job}|\t price: {job.text}")
        

        #price = job.text
        #if char in price:
        #    print(f"here this the price dipshit: {job.text}")
        #else:
        #    failCounter += 1
    
    print(failCounter)


def parseHTML(prices):
    #sm.findProducts(product, purpose)
    print("parsing html via the training data...")

    for price in prices:
            pricing = price.h5.text #finds the text in the h5 tags in course
            coursePrice = price.a.text #a stores the course price, find the text
            coursePriceParsed = coursePrice.split()[-1] #can also be denoted originally as course.a.text.split()[-1]
    print(f"pricing: {pricing}\n coursePricing: {coursePrice}\ncoursePriceParsed: {coursePriceParsed}")

def GetDomain(URL):
    websiteHTML = FindPrice(URL)
    ext = tld.extract(URL)
    domain = ext.domain
    return domain

def writeTXT(fileName, data):
    fileCreator = open(str(fileName), "w+")
    fileCreator.write(str(data))
    fileCreator.close()


def UnitTest():
    URL = "https://www.icelanticskis.com/pages/all-skis"
    #writeTXT("testDoc", "fuck")
    #print(GetDomain(URL))
    
    #parseHTML(URL)
    #print(str(FindPrice(URL)))

    htmlElement = "span"
    keyword = "money"
    GetPrice(str(FindPrice(URL)), htmlElement, keyword)

    


UnitTest()