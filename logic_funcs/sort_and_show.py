#Sort the results and print to command line:
def sortAndShow(list_of_results, priceMatch, order, max_price, min_price, search_for):
    #If there are search results:
    if len(list_of_results) > 0:
        for eachDict in list_of_results:
            #Remove '$' and ',' from price string to change to float for sorting:
            eachDict['price'] = eachDict['price'].replace("$", "")
            eachDict['price'] = eachDict['price'].replace(",", "")
    
    #Choose ascending or descending:
    if order.lower() == "d":
        list_of_results = sorted(list_of_results, reverse=True, key = lambda i: float(i['price']))
    else:
        list_of_results = sorted(list_of_results, key = lambda i: float(i['price']))

            
    #Clear acceptablePrices list in between searches:
    priceMatch.clear()
    #Go through search results:
    for item in list_of_results:
        #Keep search between price parameters:
        if float(item['price']) <= int(max_price) and float(item['price']) >= int(min_price):
            priceMatch.append(item)

    if len(priceMatch) == 0:
        print(f"No results for '{search_for}' in the range of ${min_price} and ${max_price}")
    else:
        for item in priceMatch:
            print(item['title'])
            print(item['price'])
            print(item['link'])
            print(" ")



if __name__ == "__main__":
    sortAndShow()