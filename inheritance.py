#One class (child) can inherit from another clas(parent)
#Parent Class
class Animal:
    def eat(self):
        print("Eating")

#Child Class
class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()  # Output: Eating
dog.bark()  # Output: Barking