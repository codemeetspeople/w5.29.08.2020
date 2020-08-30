def run_N_times(times):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        inner_wrapper.__name__ = func.__name__
        return inner_wrapper
    return outer_wrapper


@run_N_times(3)
def hello(username):
    print(f'Hello {username}!')


@run_N_times(5)
def point(x, y, color='black'):
    print(f'point({x}, {y}) is {color}')


print(hello.__name__)
print(point.__name__)


hello('caiman')
point(3, 5, 'black')
