from random import choice
from user_inputs.get_search_terms import getSearchTerms
from user_inputs.get_max_price import getMaxPrice
from user_inputs.get_min_price import getMinPrice
from user_inputs.get_pages import getPages
from user_inputs.get_show_order import getShowOrder
from logic_funcs.scrape_it import scrapeIt
from logic_funcs.list_filter import removeResultsWithRange
from logic_funcs.sort_and_show import sortAndShow
from logic_funcs.search_again import searchAgain
from banner_art.print_art import printArt

# --------------------------- Print ASCII Art Title -------------------------- #
#Pyfiglet colors:
eBayColors = ("red", "blue", "yellow", "green")
printArt("eBay Search And Scrape!!!", choice(eBayColors))
# ---------------------------------------------------------------------------- #
#                              MAIN LOGIC FUNCTION                             #
# ---------------------------------------------------------------------------- #

def programLoop():
    # -------------------------------- List setup -------------------------------- #
    #List to send unfiltered results to:
    rough_results = []
    #List of results with acceptable prices:
    acceptable_prices = []
    # --------------------------------- Messages --------------------------------- #
    yesOrNo = "Enter either Y or N!!!"
    nahFam = "Nah, that's not an option, fam."
    # ------------------------------- Start Program ------------------------------ #
    program_loop_stop = False
    while program_loop_stop == False:
        # ----------------------------- Get User Inputs ----------------------------- #
        search_for = getSearchTerms()
        max_price = getMaxPrice()
        min_price = getMinPrice()
        pages_to_scrape = getPages()
        order = getShowOrder()
        # ------------------------------ Function Calls ------------------------------ #
        scrapeIt(pages_to_scrape, search_for, rough_results)
        search_results = removeResultsWithRange(rough_results)
        sortAndShow(search_results, acceptable_prices, order, max_price, min_price, search_for)
        # ------------------------------- Search Again? ------------------------------ #
        search_again = searchAgain()
        if search_again:
            program_loop_stop = False
        elif search_again == False:
            program_loop_stop = True

# ---------------------------------------------------------------------------- #
#                          END OF MAIN LOGIC FUNCTION                          #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    #Let's run this thing!
    programLoop()