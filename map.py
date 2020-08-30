array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [i for i in array if i % 2 == 0]


def increment(x):
    return x + 1


def pow2(x):
    return x ** 2


def sequence_modifier(func, sequence):
    result = []

    for elem in sequence:
        result.append(func(elem))

    return result


print('Step 1')
print(array)
print(sequence_modifier(increment, array))
print(sequence_modifier(pow2, array))

print()
print('Step 2')
print(array)
print(sequence_modifier(lambda x: x + 1, array))
print(sequence_modifier(lambda x: x ** 2, array))

print()
print('Step 3')
print(array)
print(list(map(lambda x: x + 1, array)))
print(list(map(lambda x: x ** 2, array)))

print()
print('Step 4')
print(array)
print([increment(i) for i in array])
print([pow2(i) for i in array])
