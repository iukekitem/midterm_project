import json
import sys

#Check if the user forgot to provide a filename argument in the terminal
if len(sys.argv) < 2:
    print("Usage: python3 midterm_project.py <example_orders.json>")
    filename = "example_orders.json"  # Fallback to default if missing
else:
    filename = sys.argv[1]  # Grab the filename provided by the user

with open(filename, "r") as f: #open the file safely 
    orders = json.load(f) #load and parse the json into python format

print(f"Successfully loaded {len(orders)} orders from {filename}!") #confirmation

customers = {} # extract unique customers - Phone = key, name = value - No duplicates
for order in orders:
    phone = order["phone"]
    name = order["name"]
    customers[phone] = name

with open("customers.json", "w") as cf: #saves the new dict into customers.json
    customers_file = json.dump(customers, cf, indent=4) # to make it readable

print(f"Successfully exported {len(customers)} unique customers to customers.json!") #confirmation

items = {}
for order in orders:
    for item in order["items"]:
        item_name = item["name"]
        item_price = item["price"]

        if item_name not in items:
            items[item_name] = {
                "price": item_price,
                "count": 1
            }
        else:
            items[item_name]["count"] +=1


with open("items.json", "w") as il: #saves the new dict into items.json
    items_file = json.dump(items, il, indent=4) # to make it readable

print(f"Successfully exported {len(items)} unique order's name to orders.json!") #confirmation

