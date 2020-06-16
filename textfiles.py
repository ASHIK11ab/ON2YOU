import pickle

class seller:
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password

class customer:
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password

def s():
    with open("database/seller.pkl", "rb") as f:
        data = seller()
        while True:
                try:
                    data = pickle.load(f)
                    print(f"Username: {data.getusername()}  Password: {data.getpassword()}")
                except EOFError:
                    break

def c():
    with open("database/customer.pkl", "rb") as f:
        data = customer()
        while True:
                try:
                    data = pickle.load(f)
                    print(f"Username: {data.getusername()}  Password: {data.getpassword()}")
                except EOFError:
                    break

n = input("seller or customer: ")
if n=='s':
    s()
else:
    c()