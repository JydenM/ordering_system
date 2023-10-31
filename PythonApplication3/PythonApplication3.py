print ("hello what would you like to order, once you have finished your order type finish")
menu = ["pizza £7", "pie £3.45", "burger £4.50", "chips £2", "onion_rings £2.30", "drink £1.50"]
print("pizza:£7 pie:£3.45 burger:£4.50 chips:£2 onion rings:£2.30 drink:£1.50")
user_order = []
total=0.00
ordering=True
while ordering:
    item=input("what would you like to order ")
    if item == "finish":
        break
    if item == "pizza":
        user_order.append(menu[0])
        total += 7
    if item == "pie":
        user_order.append(menu[1])
        total += 3.45
    if item == "burger":
        user_order.append(menu[2])
        total += 4.50
    if item == "chips":
        user_order.append(menu[3])
        total += 2
    if item == "onion_rings":
        user_order.append(menu[4])
        total += 2.30
    if item == "drink":
        user_order.append(menu[5])
        total += 1.50
        


print (f"your order is {user_order}")
print (f"{total}")

#this programme is an ordering system which allows a use to choose items from the menu and add them to an order,
#once typing finish the programme will break the loop of repeated questions and show the user their order it will also show them a total 