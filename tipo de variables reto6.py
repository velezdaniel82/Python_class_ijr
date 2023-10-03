name = input("Type yout name: ")
amount = input("Type the amount you'd like to borrow: ")
amount_int = int(amount)
number_payments = input("Choose the total amount of payments in which you'd ike to pay the loan: ")
number_payments_int = int(number_payments)
value_each_payment = (amount_int * (1 + 0.012)) / number_payments_int
value_each_payment_str = str(value_each_payment)
print(name + ", the amount you must pay in each quote is " + value_each_payment_str)