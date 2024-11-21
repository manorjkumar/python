class animal():
    def sound(self):
        print("animal make a sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class bird(animal):
    def sound(self):
        print("birds sing")
d1=dog()
d1.sound()
b1=bird()   
b1.sound()
