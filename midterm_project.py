import json
import sys

if len(sys.argv) < 2:
    print("Usage: Python midterm_project.py <example_orders.json>")
    sys.argv[1] = "example_orders.json" 

filename = sys.argv[1]

with open(filename, "r") as f:
    orders = json.load(f)

print(f"Successfully loaded {len(orders)} orders from {filename}")