#Filter out results with range of prices:
def removeResultsWithRange(rough):
    filtered_list = []
    #Clear filtered results between searches:
    filtered_list.clear()
    for result in rough:
        to = "to"
        price = result['price']
        if to not in price:
            filtered_list.append(result)
    return filtered_list



if __name__ == "__main__":
    removeResultsWithRange()