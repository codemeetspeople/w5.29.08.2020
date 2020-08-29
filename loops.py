# array = [1,2,3,4,5]

# for item in array:
#     print(item)

# result = 1
# for elem in range(1, 11):
#     result *= elem
# print(result)

# for _ in range(5):
#     print("Hello!")

params = {1: 'alpha', 2: 'bravo', 3: 'charlie'}

for item in params:
    print(f'{item}: {params[item]}')

for key, value in params.items():
    print(f'{key}: {value}')
