from functools import reduce

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mult(x, y):
    return x * y

def sequence_reducer(func, sequence):
    result = sequence[0]

    for elem in sequence[1:]:
        result = mult(result, elem)
    
    return result

print(sequence_reducer(mult, array))
print(sequence_reducer(lambda x, y: x * y, array))
print(reduce(lambda x, y: x * y, array))