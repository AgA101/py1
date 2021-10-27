class Duck:
    def sound(self):
        print("Oaack")

class Dog:
    def sound(self):
        print("Bark")


for animal in Duck(), Dog():
    animal.sound()