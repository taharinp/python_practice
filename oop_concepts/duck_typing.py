class Duck:
    def talk(self):
        print('duck talking')

        def walk(self):
            print('duck walking')

class Dog:
    def talk(self):
        print('dog talking')

        def walk(self):
            print('dog walking')

def person(pet):
    pet.talk()
    if hasattr(pet,'walk'):
         pet.walk()

dog=Dog()
person(dog)




