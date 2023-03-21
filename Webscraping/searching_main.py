import urllib.request
import Search as s
import Webscrape as w
import webbrowser as wb
import tldextract as tld
import WebpageProcessing as wp

#start data processing---------------------------------------------------------------------------------
def GoogleProduct(product, useCase):
    searchCrit = product
    searchCrit += useCase
    print(searchCrit)

    print(f'finding resources on {product}...')
    resultsNum = 20
    resultsStop = 20
    sourceList = s.Search(searchCrit,resultsNum, resultsStop)
    #print(f'The following resources were found for {product}:\n{sourceList}')
    #print(type(sourceList))
    return sourceList

def ReadWebpage(URL):
    #print(wb.open(str(URL)))
    try: 
        webUrl = urllib.request.urlopen(URL)
        print("result code: " + str(webUrl.getcode()))
        data = webUrl.read()
        #print(data)
        return data
    except:
        print("failed to access the website successfully (see whatever code was found in the error doc)...")
        pass

def OpenWebpage(URL):
    wb.open(URL)  

def CheckRepeatURL(URL, SourceList):
    parsedUrl = tld.extract(URL)
    print(f'URL: {parsedUrl[1]}')

    URL=URL.split(" ")
 
    flag=0
    for i in URL:
        for j in SourceList:
            if i==j:
                flag=1
                break

    if flag==1:
        containSubdomain = True
    else:
        containSubdomain = False    

    #print("Does string contain any list element : "     + str(bool(res)))
    return containSubdomain

#end data processing------------------------------------------------------------------------------------ 

#start search criterion---------------------------------------------------------------------------------
def findProducts(product, purpose):
    print(f'Searching the internet for pricing on {product}...')
    purpose = purpose.lower()
    content = GoogleProduct(product, f'for {purpose}')    
    return content
#end search criterion---------------------------------------------------------------------------------


def main():
    product = "Icelantic Skis 165cm"
    #product = input("please input product: \n>")
    #SourceList = (GoogleProduct(product)) #main

    SourceList = findProducts(product)
    wb.open_new("https://www.google.com/")  
    print("---------------------------------------------------------------------------------")
    for source in SourceList:
        print(f'Finding info from: {source}')
        #ReadWebpage(source)
        OpenWebpage(source)
        #print(f'was the string contain the element?....................................... {CheckRepeatURL(source, SourceList)}'
    print("---------------------------------------------------------------------------------")

def UnitTest():
    #product = "Icelantic Skis" #basic
    product = "Icelantic Skis 165cm" #medium complicated
    #product = "Icelantic Skis 165cm 100 underfoot" #high complicated

    purpose = "cheap"
    
    print(f'performing unit testing...\n')
    SourceList = findProducts(product, purpose)

    for source in SourceList:
        print(f'Finding info from: {source}')
        #ReadWebpage(source)
        #OpenWebpage(source)
        #print(f'was the string contain the element?....................................... {CheckRepeatURL(source, SourceList)}'
    print("---------------------------------------------------------------------------------")

    
UnitTest()