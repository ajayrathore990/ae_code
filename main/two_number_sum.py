"""
Category: Arrays
"""

def number_sum_two(array,target):
    values= {}
    for i  in array:
        v = target- i 
        if v in values:
            return [v,i]
        else:
            values[i] = True
    return []


def number_sum_two_(array,target):
    for i in range(len(array)-1):
        first_number = array[i]
        for j in range(i+1,len(array)):
            second_number = array[j]
            if first_number + second_number ==target:
                return [first_number,second_number]
    return []
         
