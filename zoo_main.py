from importlib import reload
from zoo.delivery import deliver
from zoo import animals


def main():
    while True:
        print('Hello! Welcome into the zoo!')

        available_animals = ' '.join(animals.ANIMALS.keys())

        print(f'Available animals: {available_animals}')
        action = input().strip().lower()

        if action == 'exit':
            print('Bye! Bye!')
            exit()

        if action in animals.ANIMALS.keys():
            animals.ANIMALS[action].speak()
        else:
            deliver(action)
            reload(animals)

        print()
        print()


try:
    main()
except KeyboardInterrupt:
    print('Bye! Bye!')
