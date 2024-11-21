'''class compan  y():
    def __init__(self):
        self.__companyname="google"
    def companyname(self):
        print(self.__companyname)

c1=company()
c1.companyname()'''

try:
    a=int(input())
    b=int(input())#if we enter integer instant of string we get value error
    c=input()
    #print(c/a)#if we try to divided by int and str we get typr error
    print(d)#here we try to print d value we get NameError because we not define d
except Exception as e:#it will work for every error
    print("something worng",e)
except ValueError as e:
    print("valur error",e)
except TypeError as e:
    print("typr error",e)
except NameError as e:  
    print("Name Error",e)
except Exception:
    print("something worng")
finally:
    print("everything is done")
