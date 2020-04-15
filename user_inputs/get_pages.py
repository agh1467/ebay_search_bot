def getPages():
    yesOrNo = "Enter either Y or N!!!"
    nahFam = "Nah, that's not an option, fam."
    #Ask how many pages to scrape:
    pages_to_scrape = input("How many pages would you like to scrape?: ")
    while type(pages_to_scrape) == str:
        try:
            pages_to_scrape = int(pages_to_scrape)
            if int(pages_to_scrape):
                break
        except ValueError:
            print(" ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("You have to enter an integer!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            pages_to_scrape = input("How many pages would you like to scrape?: ")
    return pages_to_scrape



if __name__ == "__main__":
    getPages()