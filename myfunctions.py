import pickle

class seller:
    def getusername(self):
        return self.username

    def getpassword(self):
        return self.password

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

def newuser(action, name, password):
    if action == "s":
        obj = seller()
        is_new = True
        with open("seller.pkl", "a+b") as file:
            while True:
                try:
                    obj = pickle.load(file)
                    if obj.getusername() == name:   #Checking if there exists a user with the chosen username.
                        is_new = False
                        break
                except EOFError:
                    break
        if is_new:  #if new user add this seller to database 'seller.pkl'
            with open("seller.pkl", "a+b") as f:
                object = seller()
                object.username = name
                object.password = password
                pickle.dump(object, f)
        return is_new
