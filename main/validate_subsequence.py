"""
Category: Arrays
"""

def correct_subsequence(array,sequence):
    arr_id = 0
    seq_id = 0
    while arr_id< len(array) and seq_id< len(sequence):
        if array[arr_id] == sequence[seq_id]:
            seq_id =seq_id + 1
        arr_id= arr_id +1
    return seq_id == len(sequence)


def correct_subsequence_(array,sequence):
    seq_id = 0
    for value in array:
        if seq_id ==len(sequence):
            break
        if sequence[seq_id] ==value:
            seq_id = seq_id+1
    return seq_id == len(sequence)