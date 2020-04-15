def getMaxPrice():
    yesOrNo = "Enter either Y or N!!!"
    nahFam = "Nah, that's not an option, fam."
    #Ask max price:
    max_price_prompt = input("Would you like to set a maximum price? (Y/N): ")
    maxLoopStop = False
    while maxLoopStop == False:
        if max_price_prompt.lower() == "n":
            maxLoopStop = True
            max_price = 10000000
        elif max_price_prompt.lower() == "y":
            max_price = input("What is the most you are willing to spend: $")
            maxLoopStop = True
            max_price = int(max_price)
        else:
            print(" ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(yesOrNo)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            max_price_prompt = input("Would you like to set a maximum price? (Y/N): ")

    return max_price


if __name__ == "__main__":
    getMaxPrice()