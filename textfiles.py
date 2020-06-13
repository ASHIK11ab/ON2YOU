import pickle

class seller:
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password

with open("seller.pkl", "rb") as f:
    data = seller()
    while True:
            try:
                data = pickle.load(f)
                print(f"Username: {data.getusername()}  Password: {data.getpassword()}")
            except EOFError:
                break
def existinguser(action, name,password):
    if action == "s":
        obj = seller()
        is_existing = False
        with open("seller.pkl", "rb") as file:
            while True:
                try:
                    obj = pickle.load(file)
                    if obj.getusername() == name:       #Checking for an existing user
                        if obj.getpassword() == password:
                            is_existing = True
                            break
                        else:
                            break
                except EOFError:
                    break
        return is_existing
print(existinguser('s','Meeranbj','456'))