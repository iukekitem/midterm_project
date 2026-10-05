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

print(f"Successfully loaded {len(orders)} orders from {filename}") #confirmation