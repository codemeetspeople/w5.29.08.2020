from string import ascii_lowercase
import random

from . import settings

PATTERN = (
    '\n@animal_in_zoo\n'
    'class {classname}(Animal):\n'
    '    @classmethod\n'
    '    def speak(cls):\n'
    '        print(f\'{{cls.get_title()}} say {sound}-{sound}\')\n\n'
)


def deliver(animal):
    sound = ''.join([random.choice(ascii_lowercase) for _ in range(4)])

    animal_cls = PATTERN.format(
        classname=animal.capitalize(),
        sound=sound
    )

    with open(settings.ZOO_ANIMALS, 'r') as file:
        data = file.read()

    complete_data = f'{data}\n{animal_cls}'

    with open(settings.ZOO_ANIMALS, 'w') as file:
        file.write(complete_data)
