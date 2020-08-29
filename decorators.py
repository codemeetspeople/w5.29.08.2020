def run_5_times(func):
    def wrapper(*args, **kwargs):
        for _ in range(5):
            func(*args, **kwargs)
    
    return wrapper


@run_5_times
def hello(username):
    print(f'Hello {username}!')

@run_5_times
def point(x, y, color='black'):
    print(f'point({x}, {y}) is {color}')


hello('caiman')

point(3, 5, 'blue')
