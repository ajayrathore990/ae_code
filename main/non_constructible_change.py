def non_constructible_change(array):
    array.sort()
    change= 0
    for coin in array:
        if coin > change + 1:
            return change + 1
        change = change + coin 
    return change + 1

