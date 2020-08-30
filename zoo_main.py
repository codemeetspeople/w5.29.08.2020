from zoo.delivery import deliver
from zoo.animals import ANIMALS


def main():
    while True:
        print('Hello! Welcome into the zoo!')

        available_animals = ' '.join(ANIMALS.keys())

        print(f'Available animals: {available_animals}')
        action = input().strip().lower()

        if action == 'exit':
            print('Bye! Bye!')
            exit()

        if action in ANIMALS.keys():
            ANIMALS[action].speak()
        else:
            deliver(action)
        
        print()
        print()

try:
    main()
except KeyboardInterrupt:
    print('Bye! Bye!')
