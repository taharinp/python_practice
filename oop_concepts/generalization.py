class Animal:        # General Class
    def eat(self):
        print("Animal eats")

class Dog(Animal):   # Specific Class
    def bark(self):
        print("Dog barks")

class Cat(Animal):   # Specific Class
    def meow(self):
        print("Cat meows")


d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()