class student:
    def __init__(self):
        self.name="manoj"
        self.register_num="XXX"

    def display(self):
        print("name: ",self.name)
        print("register_num: ",self.register_num)

s1=student()
s1.display()

ss1=student()
ss1.name="john"
ss1.register_num="12XX43"

ss1.display()
print("ss1 name: ",ss1.name)


class fruit:
    def __init__(self):
        self.color=""

apple=fruit()
apple.color="red"
print("apple color: ",apple.color)


class teacher:
    def __init__(self,t1name,t1regno):
        self.name=t1name
        self.regno=t1regno
    def display(self):
        print("teacher's name: ",self.name)
        print("teacher's regno: ",self.regno)
print("--------------teacher1 details-------------")
t1=teacher("keerthana","12XX23")
t1.display()
print("--------------teacher2 details-------------")
t2=teacher("nisha","21XX43")
t2.display()

class calculator:
    def __init__(self,v1,v2):
        self.num1=v1
        self.num2=v2
    def add(self):
        c=self.num1+self.num2
        print("added value: ",c)
    def mul(self):
        d=self.num1*self.num2
        print("multiple value: ",d)
    def sub(self):
        e=self.num1-self.num2
        print("suprate value: ",e)
    def div(self):
        f=self.num1/self.num2
        print("division value: ",f)
    

obj1=calculator(4,4)
obj1.add()
obj1.mul()
obj1.sub()
obj1.div()

        
    
    
