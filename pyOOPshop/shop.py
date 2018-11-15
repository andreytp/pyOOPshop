class Shop:
    def __init__(self):
        self.shopname = "All4lanch"
        
        self.regular_customers = {"John Dou": 0.1, "Jack Sparrow":0.3, "Billy Bounce":0.05}
        
        self.price = {"butter":{"price":5, "discount":0.1}, "ham":{"price":15, "discount":0.05}, "bread":{"price":3, "discount":0.01}, "coffee":{"price":10, "discount":0.07}}
        
        self.time_discount = {"7": 0.02, "21": 0.25, "23":-0.25}

    def actual_cost(self, customer, product, hour):
        if customer == "Chuck Norris":
            return -1000

        pricepos = self.price.get(product)
        if pricepos == None:
            #print("good {} not found".format(product))
            return 0
        
        cost = pricepos.get("price", 0)
        if cost == 0:
            return 0

        pricediscount = pricepos.get("discount",0)

        customerdiscount = self.regular_customers.get(customer,0)

        timediscount = self.time_discount.get(hour,0)
    
        return round(cost*(1-pricediscount)*(1-customerdiscount)*(1-timediscount), 2)
