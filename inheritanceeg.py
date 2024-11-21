'''class grandpa():
    def phone(self):
        print("granpa's mobile")
class familybussiness():
    def bussiness(self):
        print("it's a family business")
class dad(grandpa,familybussiness):
    def money(self):
        print("dad's money")
class son1(dad,grandpa):
    def laptop(self):
        print("son's laptop")

manoj =son1
manoj.laptop()
manoj.money()
manoj.phone()
manoj.bussiness()'''

class a():
    def __init__(self):
        print("class a")
    def display(self):
        print("you are in a class")
class b():
    def __init__(self):
        super().__init__()
        print("class b")
    def display(self):
        print("you are in b class")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("class c")
    def display(self):
        print("you are in c class")

obj1=c()
