__author__ = 'artur'

class animal:
    def __init__(self):
        pass
    def make_sound(self):
        print("gav gav")

class cat(animal):
    def make_sound(self):
        print("mew")

print("Hello world")
c = animal()
c.make_sound()
c.name = "Murzik"

print(dict(c))

