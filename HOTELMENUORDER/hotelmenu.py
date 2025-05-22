
# Define the menu of restaurant
menu = {
    'Maharashtrian Veg Thali':	120,
    'Special Veg Thali':	    160,
    'Bhakri Thali (2 Bhakris)':	130,
    'Pithla Bhakri':	        100,
    'Zunka Bhakri':	            90,
    'Chapati Bhaji Plate':	    80,
    'Varan Bhat + Papad':       70,
    'Matki Usal + Bhakri': 	    110,
}

# Greet
print("WELCOME TO PYTHON RESTAURANT //Bhakri House//")
print(" /n Maharashtrian Veg Thali:120\n Special Veg Thali:160\n Bhakri Thali (2 Bhakris):130, \n Pithla Bhakri:100,\n Zunka Bhakri:90,\n Chapati Bhaji Plate:80,\n Varan Bhat + Papad:70,\n Matki Usal + Bhakri:110")

order_total = 0 
#80 + 70 = 150

item_1 = input(" Enter the name of name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 500
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaiable yet !")


another_order = input("DO you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable yet !")

another_order = input("DO you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_3 = input ("Enter the name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item {item_3} has been added to order")

    else:
        print(f"Ordered item {item_3} is not avaialable yet !")

another_order = input("DO you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_4 = input ("Enter the name of fourth item = ")
    if item_4 in menu:
        order_total += menu[item_4]
        print(f"Item {item_4} has been added to order")

    else:
        print(f"Ordered item {item_4} is not avaialable yet !")

print(f"The total amount of item to pay is {order_total}")