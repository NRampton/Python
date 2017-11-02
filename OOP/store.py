class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_rate):
        if tax_rate >= 1:
            return self.price + self.price * (tax_rate / 100)
        if tax_rate < 1:
            return self.price + self.price * tax_rate

    def make_return(self, note):
        if note == "defective":
            self.status = "defective"
            self.price = 0
        elif note == "in box":
            self.status = "for sale"
        elif note == "open box":
            self.status = "used"
            self.price = self.price - (self.price * 0.2)
        return self

    def display_info(self):
        print "Product name: {}".format(self.name)
        print "Product brand:", self.brand
        print "Price: ${}".format(self.price)
        print "Item weight {}oz.".format(self.weight)
        print "Item status:", self.status


class Store(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.products = []

    def add_product(self, price, name, weight, brand):
        new_product = Product(price, name, weight, brand)
        self.products.append(new_product)
        print "Successfully added {}.".format(new_product.name)
        print "Shelves now contain the following:"
        for product in self.products:
            print "\t" + product.name

    def remove_product(self, query_name):
        for product in range(len(self.products)):
            if self.products[product].name == query_name:
                del self.products[product]
                break
        print "Removed {}".format(query_name)
        print "Shelves now contain the following:"
        for product in self.products:
            print "\t" + product.name


store1 = Store("GarbageMart", "Oscar T Grouch")
store1.add_product(3.50, "Garbage", 100, "Grouch-o")
store1.add_product(4.50, "More Garbage", 200, "Grouch-o")
store1.add_product(5.50, "Family-size Garbage Pail", 400, "Grouch-o")
store1.remove_product("More Garbage")
