import shop

obj_shop = shop.Shop()
customer_list = ["John Dou", "Chuck Norris", "Jack Sparrow", "Charles Freddy Krueger", "Billy Bounce"]
goods_list = ["butter","ham","beer", "bread", "cake", "coffee"]
hours_list = ["6","7","8","11","13","15","18","21","23"]

for good in goods_list:
    for hour in hours_list:
        for customer in customer_list:
        
            paid_sum = obj_shop.actual_cost(customer,good,hour)
            
            if paid_sum == 0:
                continue

            description = ""
            if paid_sum < 0:
                description = ", because he is {}".format(customer)

            print("In {} mr. {} paid {}$ for {} at {} hour{}".format(obj_shop.shopname, customer, paid_sum, good, hour, description))