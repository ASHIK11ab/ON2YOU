import pickle

class products:
    def getusername(self):
            return self.username

    def getitem_name(self):
        return self.item_name

    def getcategory(self):
        return self.category

    def getcost(self):
        return self.cost

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

user = input("username: ")
results, total = get_all_products(user)
print("products: \n",results)
print("total: ",total)