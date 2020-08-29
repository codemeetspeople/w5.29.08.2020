def my_range(*args):
    args_count = len(args)
    if args_count < 1 or args_count > 3:
        raise ValueError()

    step = 1
    if args_count == 1:
        start, end = 0, args[0]
    elif args_count == 2:
        start, end = args
    else:
        start, end, step = args

    while start < end:
        yield start
        start += step


print('my_range(5):')
for i in my_range(5):
    print(i)
print()

print('my_range(2, 7):')
for i in my_range(2, 7):
    print(i)
print()

print('my_range(1, 10, 2):')
for i in my_range(1, 10, 2):
    print(i)
print()