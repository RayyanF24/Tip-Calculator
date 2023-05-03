#Python Tip Calculator the tax part is ONLY for Ontario Residents
#Made by Rayyan Faisal 
print("Welcome to Rayyan's tip Caclculator, this for ONLY Ontario residents")
#cost of the meal
meal_amount= input("Please enter the price of your meal in $")
#how much tip is being given, PLEASE enter a whole number percentage
tip= input("How much tip you would like to give in percentage? Pls enter a whole number %")
#tax amount only for Ontario residents, can vary from locations
tax_amount= 13.0/100
#find the total amount with the tip without tax
total_tip = float(meal_amount) * (1.0 + (float(tip)/100.0))
#total tax added to the bill
total_tax = float(meal_amount) * tax_amount
#total cost of meal
total_cost = total_tip + total_tax
print ("The cost of the meal was $"+ meal_amount )
print ("The total money you should bring for the restaurant including tax and the tip is $"+ str(total_cost))
