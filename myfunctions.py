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

class products:
    def getusername(self):
            return self.username

    def getitem_name(self):
        return self.item_name

    def getcategory(self):
        return self.category

    def getcost(self):
        return self.cost

def existingseller(name,password):
        obj = seller()
        is_existing = False
        with open("database/seller.pkl", "rb") as file:
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

def newseller(name, password):
        obj = seller()
        is_new = True
        with open("database/seller.pkl", "rb") as file:
            while True:
                try:
                    obj = pickle.load(file)
                    if obj.getusername() == name:   #Checking if there exists a user with the chosen username.
                        is_new = False
                        break
                except EOFError:
                    break
        if is_new:  #if new user add this seller to database 'seller.pkl'
            with open("database/seller.pkl", "a+b") as f:
                object = seller()
                object.username = name
                object.password = password
                pickle.dump(object, f)
        return is_new

def existingcustomer(name,password):
        obj = customer()
        is_existing = False
        with open("database/customer.pkl", "r+b") as file:
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

def newcustomer(name, password):
        obj =customer()
        is_new = True
        with open("database/customer.pkl", "rb") as file:
            while True:
                try:
                    obj = pickle.load(file)
                    if obj.getusername() == name:   #Checking if there exists a user with the chosen username.
                        is_new = False
                        break
                except EOFError:
                    break
        if is_new:  #if new user add this seller to database 'seller.pkl'
            with open("database/customer.pkl", "a+b") as f:
                object = customer()
                object.username = name
                object.password = password
                pickle.dump(object, f)
        return is_new

def update_database(myproducts, username):
    obj = products()
    with open('database/products.pkl', "a+b") as file:
        obj.username = username
        obj.item_name = myproducts["item_name"]
        obj.category = myproducts["category"]
        obj.cost = myproducts["cost"]
        pickle.dump(obj, file)

def get_all_products(username):
    cnt = 0
    results = {}
    obj = products()
    with open('database/products.pkl', 'rb') as file:
        while True:
            try:
                obj = pickle.load(file)
                if obj.getusername() == username:
                    subresults = {}
                    cnt+= 1
                    subresults["item_name"] = obj.getitem_name()
                    subresults["category"] = obj.getcategory()
                    subresults["cost"] = obj.getcost()
                    results[cnt] = subresults
            except EOFError:
                break
    return (results,cnt)

def recentproduct(username):
    obj = products()
    recent = {}
    cnt = 0
    with open('database/products.pkl', 'rb') as file:
        while True:
            try:
                obj = pickle.load(file)
                if obj.getusername() == username:
                    cnt+= 1
                    recent["item_name"] = obj.getitem_name()
                    recent["category"] = obj.getcategory()
                    recent["cost"] = obj.getcost()
            except EOFError:
                break
    return (recent, cnt)
