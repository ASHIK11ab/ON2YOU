import pickle
import datetime
import random
import os


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


def existingseller(name, password):
    obj = seller()
    is_existing = False
    with open("database/seller.pkl", "rb") as file:
        while True:
            try:
                obj = pickle.load(file)
                if obj.getusername() == name:  # Checking for an existing user
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
                # Checking if there exists a user with the chosen username.
                if obj.getusername() == name:
                    is_new = False
                    break
            except EOFError:
                break
    if is_new:  # if new user add this seller to database 'seller.pkl'
        with open("database/seller.pkl", "a+b") as f:
            object = seller()
            object.username = name
            object.password = password
            pickle.dump(object, f)
    return is_new


def existingcustomer(name, password):
    obj = customer()
    is_existing = False
    with open("database/customer.pkl", "r+b") as file:
        while True:
            try:
                obj = pickle.load(file)
                if obj.getusername() == name:  # Checking for an existing user
                    if obj.getpassword() == password:
                        is_existing = True
                        break
                    else:
                        break
            except EOFError:
                break
    return is_existing


def newcustomer(name, password):
    obj = customer()
    is_new = True
    with open("database/customer.pkl", "rb") as file:
        while True:
            try:
                obj = pickle.load(file)
                # Checking if there exists a user with the chosen username.
                if obj.getusername() == name:
                    is_new = False
                    break
            except EOFError:
                break
    if is_new:  # if new user add this seller to database 'seller.pkl'
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
                    cnt += 1
                    subresults["item_name"] = obj.getitem_name()
                    subresults["category"] = obj.getcategory()
                    subresults["cost"] = obj.getcost()
                    results[cnt] = subresults
            except EOFError:
                break
    return (results, cnt)


def recentproduct(username):
    obj = products()
    recent = {}
    cnt = 0
    with open('database/products.pkl', 'rb') as file:
        while True:
            try:
                obj = pickle.load(file)
                if obj.getusername() == username:
                    cnt += 1
                    recent["item_name"] = obj.getitem_name()
                    recent["category"] = obj.getcategory()
                    recent["cost"] = obj.getcost()
            except EOFError:
                break
    return (recent, cnt)


def recent_products_find():
    cnt = 0
    results = {}
    obj = products()
    with open('database/products.pkl', 'rb') as file:
        while True:
            try:
                obj = pickle.load(file)
                subresults = {}
                cnt += 1
                subresults["seller_name"] = obj.getusername()
                subresults["item_name"] = obj.getitem_name()
                subresults["category"] = obj.getcategory()
                subresults["cost"] = obj.getcost()
                results[cnt] = subresults
            except EOFError:
                break
    return (results, cnt)


def generateid():
    id = random.randrange(1, 100000)
    return id


def generatebill(product, username):
    now = datetime.datetime.now()
    product["date"] = now.date()
    flag = 0
    cnt = 0
    with open("database/id.pkl", "rb") as file:
        existing_ids = []
        while True:
            try:
                existing_ids = pickle.load(file)
                cnt += 1
                while True:
                    id = generateid()
                    print("id is: ", id)
                    if id not in existing_ids:
                        product["bill_id"] = id
                        existing_ids.append(id)
                        flag = 1
                        break
            except EOFError:
                break
    if cnt == 0:
        id = generateid()
        product["bill_id"] = id
        existing_ids.append(id)
        flag = 1
        print("id is: ", id) 

    if flag == 1:
        with open('database/id.pkl', "wb") as file:
            pickle.dump(existing_ids, file)

        with open('database/bill.pkl', "ab") as file:
            pickle.dump(product, file)

    if product["mode"] == 'cart':
        with open('database/cart.pkl', "rb") as source:
            with open('database/temporary.pkl', "wb") as destination:
                while True:
                    try: 
                        data = pickle.load(source)
                        if data["customer_name"] != username:
                            pickle.dump(data, destination)
                    except EOFError:
                        break
        os.chdir('database')
        os.remove('cart.pkl')
        os.rename('temporary.pkl','cart.pkl')
        os.chdir('../')
        
def getmybill_ids(username):
    with open("database/bill.pkl", "rb") as file:
        id = []
        cnt = 0
        while True:
            try:
                data = pickle.load(file)
                if data["customer_name"] == username:
                    id.append(data["bill_id"])
                    cnt += 1
            except EOFError:
                break
    return id, cnt


def get_this_bill(bill_id, username):
    with open("database/bill.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["bill_id"] == int(bill_id):
                    item = data
            except EOFError:
                break    
    return item


def add_this_product_to_cart(product):
    with open("database/cart.pkl", "ab") as file:
        pickle.dump(product, file)


def my_items_in_cart(username):
    results = {}
    cnt = 0
    cost = 0
    with open("database/cart.pkl", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["customer_name"] == username:
                    cnt += 1
                    results[cnt] = data
                    cost += data["total_cost"]
            except EOFError:
                break
    return (results, cnt, cost)
