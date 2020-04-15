def getMinPrice():
    yesOrNo = "Enter either Y or N!!!"
    nahFam = "Nah, that's not an option, fam."
    #Ask min price:
    min_price_prompt = input("Would you like to set a minimum price? (Y/N): ")
    minLoopStop = False
    while minLoopStop == False:
        if min_price_prompt.lower() == "n":
            min_price = 0
            minLoopStop = True
        elif min_price_prompt.lower() == "y":
            min_price = input("Enter your minimum price: $")
            min_price = int(min_price)
            minLoopStop = True
        else:
            print(" ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(yesOrNo)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            min_price_prompt = input("Would you like to set a minimum price? (Y/N): ")
    return min_price


if __name__ == "__main__":
    getMinPrice()