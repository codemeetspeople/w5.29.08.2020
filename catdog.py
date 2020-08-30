class Cat:
    def meow(self):
        print(f'{self.__class__.__name__} say meow...')

    def eats(self):
        print(f'{self.__class__.__name__} eats fish...')


class Dog:
    def bark(self):
        print(f'{self.__class__.__name__} say grrr...')

    def eats(self):
        print(f'{self.__class__.__name__} eats meat...')


class CatDog(Dog, Cat):
    def eats(self):
        print(f'{self.__class__.__name__} eats meat and fish...')


catdog = CatDog()
catdog.eats()
super(CatDog, catdog).eats()
# super(Dog, catdog).eats() #! What the fuck!?
