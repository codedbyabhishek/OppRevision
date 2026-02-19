#Object can take multiplel froms. Methods with the same name can behave differently based on the object that is calling them. This is called polymorphism.  
class Bird:
    def sound(self):
        print("Chirp Chrirp")
class parrot(Bird):
    def sound(self):
        print("Squawk Squawk")

b = Bird()
p = parrot()
b.sound()
p.sound()