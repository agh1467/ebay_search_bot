import requests
from bs4 import BeautifulSoup
from logic_funcs.page_num_plus import pageNumPlus
from time import sleep
#Scraper function:
def scrapeIt(num_of_pages, search_for, roughResults):
    yesOrNo = "Enter either Y or N!!!"
    nahFam = "Nah, that's not an option, fam."
    #Base url to scrape:
    baseURL = "https://www.ebay.com"
    #Search url (/sch/) with Buy It Now (&LH_BIN=1) and page-url beginning:
    searchURL = f"/sch/{search_for}&LH_BIN=1&_pgn="
    pageNum = "1"
    #URL all put together:
    url = f"{baseURL}{searchURL}{pageNum}"
    #Page count:
    count = num_of_pages
    #Clear rough results list between searches:
    roughResults.clear()
    while count > 0:

        #Make http request:
        response = requests.get(f"{url}")
        print(f"Now scraping: {url}")
        print(" ")
        #Send through Beautiful Soup:
        soup = BeautifulSoup(response.text, "html.parser")
        #Search Results
        results = soup.find_all(class_="s-item")

        #Assign Keys:
        for result in results:
            try:
                #Send to list:
                roughResults.append({
                    "title": result.find(class_="s-item__title").get_text(),
                    "price": result.find(class_="s-item__price").get_text(),
                    "link": result.find(class_="s-item__link")["href"]
                })
            #Catch AttrErrors and pass by:
            except AttributeError:
                pass

        #Increase page number:
        pageNum = pageNumPlus(pageNum)
        #Reset url:
        url = f"{baseURL}{searchURL}{pageNum}"
        count -= 1
        #Give ten seconds before requesting next page
        sleep(5)

    return roughResults



if __name__ == "__main__":
    scrapeIt()