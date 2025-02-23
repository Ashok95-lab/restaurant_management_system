# Menu list with Price
menu = {
    'Tea': 30,
    'Onion Masala Dosa': 140,
    'Veg Puff': 20,
    'Plain Dosa': 105,
    'Onion Cheese Masala Dosa': 160,
    'Coffee': 40,
    'Mirchi Pakoda': 20,
    'Butter Onion Masala Dosa': 160,
    'Kesariya Tea': 40,
    'Masala Tea': 30,
    'Aloo Bonda': 20,
    'Paneer Pakoda': 25,
    'Butter Paper Masasala': 190,
    'Paper Plain Dosa': 150,
    'Schezwan Plain Dosa': 160,
    'Radha Ballavi': 70,
    'Raj Kachori Chaat': 85,
    'Club Kachori': 50,
    'Papdi Chaat': 75,
    'Butter Cheese Plain Dosa': 140,
    'Butter Cheese Onion': 230,
    'Khasta Kachori Chaat': 80,
    'Butter Cheese Onion Plain Dosa': 150,
    'Plain Idly': 65,
    'Dhokla Chaat': 70,
    'Idly+Vada Combo (1+1)': 75,
    'Dahi Samosa Chaat': 80,
    'Veg Grilled Sandwich': 80,
    'Butter Paper Plain Dosa': 170,
    'Sambhar Vada': 75,
    'Mix Chat': 100,
    'Veg Cheese Grilled': 105,
    'Cheese Paper Plain Dosa': 180,
    'Chola Samosa Chaat': 85,
    'Onion Uttapam': 130,
    'Butter Cheese Paper': 200,
    'Veg Sandwich': 70,
    'Dahi Vada': 65,
    'Tomato Uttapam': 140,
    'Malai Toast': 50,
    'Masala Dosa': 130,
    'Mixed Uttapam': 160,
    'Butter Masala Dosa': 150,
    'Cheese Masala Dosa': 150,
    'Lassi': 60,
    'Chola Bhatura': 115,
    'Samosa': 16,
    'Butter Cheese Masala': 170,
    'Pav Bhaji': 90,
    'Masala Dosa': 150,
    'Malai Lassi': 75,
    'Khasta Kachori': 17,
    'Extra Bhatura': 40,
    'Mandal Special Masala Dosa': 190,
    'Kesar Lassi': 80,
    'Dhokla': 35,
    'Extra Pav': 25,
    'Mysore Masala Dosa': 160,
    'Masala Lassi': 70,
    'Veg Cutlet': 20,
    'Extra Chola': 25,
    'Pizza Dosa': 170,
    'Plain Lassi': 70,
    'Bikaneri Patties': 20,
    'Schezwan Masala Dosa': 180,
    'Bread Pakora': 30,
    'Butter Milk': 60
}

print("Welcome to our Mandal Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

order_total = 0

# Infinite loop to allow unlimited orders
while True:
    item = input("Enter the name of item you want to order (or type 'done' to finish): ")

    if item.lower() == 'done':
        break  # Exit loop if user types 'done'

    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Ordered item {item} is not available")

# Final amount will be displayed here
print(f"The total amount is Rs {order_total} /-")
print("Thank you for visiting Mandal Restaurant. Have a great day!")
