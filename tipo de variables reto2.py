table_number = input("Introduce your table number: ")
product_cost = input("Introduce the gross cost of your product: ")
product_cost_int = int(product_cost)
tax_value = product_cost_int*0.1
net_cost = product_cost_int + tax_value
tax_value_str = str(tax_value)
net_cost_str = str(net_cost)
print("The cost of the product demanded by table #" + table_number + " is $" + product_cost + " plus a 10% tax equal to " + tax_value_str + " and a total cost of " + net_cost_str)
