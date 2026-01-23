
def array_of_product(array):
    result = len(array)* [1]
    for i in range(len(array)):
        running_total =1
        for j in range(len(array)):
            if i !=j:
                running_total = running_total * array[j]
        result[i] = running_total
    return result
    
def array_of_product_(array):
    product =1
    result_ =[]
    for i in array:
        product=product*i
    result = [product]* len(array)
    
    for i in range(len(array)):
        try:
            result_.append(int(result[i]/array[i]))
        except ZeroDivisionError as e:
            return [0]* len(array)
    
    return result_

