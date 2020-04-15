def getShowOrder():
    yesOrNo = "Enter either Y or N!!!"
    nahFam = "Nah, that's not an option, fam."
    reverse_check_prompt = input("In what order would you like your results? ('a' for Ascending/'d' for Descending): ")
    reverse_prompt_loop_stop = False
    while reverse_prompt_loop_stop == False:
        if reverse_check_prompt.lower() == "a" or reverse_check_prompt.lower() == "d":
            reverse_prompt_loop_stop = True
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(nahFam)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            reverse_check_prompt = input("In what order would you like your results? ('a' for Ascending/'d' for Descending): ")
    return reverse_check_prompt



if __name__ == "__main__":
    getShowOrder()