'''def add():
   a=int(input("enter a value"))
   b=int(input("enter b value "))
   c=a+b
   return c
ans=add()
print(ans)'''

m_username="manojkumar"
m_password="123456"

username=input("enter username: ")
password=input("enter your password: ")

def validate():
    if(m_username== username and m_password==password ):
        return "successfully login"
    else:
        return "Worng username&password"
result=validate()
print(result)
