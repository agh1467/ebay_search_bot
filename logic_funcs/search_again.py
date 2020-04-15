def searchAgain():
    nahFam = "Nah, that's not an option, fam."
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    search_again_loop_stop = False
    while search_again_loop_stop == False:
        search_again = input("Would you like to search again? (Y/N): ")
        if search_again.lower() == "y":
            search_again_loop_stop = True
            return_val = True
        elif search_again.lower() == "n":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Ok... See you later, bruv!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            search_again_loop_stop = True
            return_val = False
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(nahFam)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return return_val



if __name__ == "__main__":
    searchAgain()