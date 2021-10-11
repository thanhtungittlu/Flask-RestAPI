class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_item(self, name,price):
        store_dict = {"name": name, "price":price}
        self.items.append(store_dict)
    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item["price"]
        # return total
        return sum([item["price"] for item in self.items])
    @classmethod
    def franchise(cls,self):
        return cls(self.name + " - franchise ")
 
    @staticmethod
    def store_details(self):
        print("{}, total stock price: {}" .format(self.name, self.stock_price() ))
         
store = Store("Alibaba")
store2 = Store("Amazon")
store2.add_item("Keyboard",160)

a = Store.franchise(store) #return: "Alibaba - franchise"
print(a.name)
b = Store.franchise(store2) #return: "Amazon - franchise"
print(b.name)

Store.store_details(store)
Store.store_details(store2)

