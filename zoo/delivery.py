from . import settings

def deliver(animal):
    print(f'{animal} would be delivered into {settings.ZOO_ANIMALS}')
