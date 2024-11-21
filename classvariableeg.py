class laptop():
    chargertyp="c Type"
    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
        
    @classmethod
    def changechargertype(cls):
        cls.chargertype="b type"
        print("charger typt changed to b")
        
    @staticmethod
    def info():
        print("This is laptop class")

hp=laptop()
hp.getprice()
hp.getprice()

laptop.changechargertype()

hp.info()
