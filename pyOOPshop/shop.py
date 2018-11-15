class Shop:
    regular_customers = {}
    price = {}
    time_discount = {}
    def __init__(self):
        self.regular_customers.fromkeys("John Dou", 0.1)
        self.regular_customers.fromkeys("Jack Sparrow", 0.3)
        self.regular_customers.fromkeys("Billy Bounce", 0.05)
        
        self.price.fromkeys("butter", {"price":5, "discount":0.1})
        self.price.fromkeys("ham", {"price":15, "discount":0.05})
        self.price.fromkeys("bread", {"price":3, "discount":0.01})
        self.price.fromkeys("coffee", {"price":10, "discount":0.07})

        self.time_discount.fromkeys(7,0.02)
        self.time_discount.fromkeys(21,0.25)

    def actual_cost(customer, product, hour):
        

        
        return 0


