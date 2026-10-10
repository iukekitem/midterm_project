# Midterm Project

This repository contains `midterm_project.py`, a small script that processes an orders JSON file and exports two summary files: `customers.json` and `items.json`.

**What it does:**
- **Input:** reads an orders JSON file (a list of order objects).
- **Customers export:** extracts unique customers (keyed by phone) and writes `customers.json` mapping phone → name.
- **Items export:** aggregates ordered items by name and writes `items.json` where each item has `price` and `count`.

**Design / implementation notes:**
- The script checks for a command-line filename argument. If none is provided it falls back to `example_orders.json`.
- It loads the JSON with `json.load()` into a Python object named `orders`.
- It iterates `orders` once to build a `customers` dict where the phone number is the dictionary key and the customer name is the value (this deduplicates customers by phone).
- It iterates the orders again to aggregate `items` by `name`, storing `price` and `count` for each item name.
- Finally it writes `customers.json` and `items.json` using `json.dump(..., indent=4)` for readability.

**Expected input format**
- The input file should contain a JSON array of order objects. Each order should include at least these keys:
  - `name` (string): customer name
  - `phone` (string): customer phone, used as unique identifier
  - `items` (array): list of item objects; each item must include `name` (string) and `price` (number)

Example single-order object:

```json
{
  "name": "Jane Doe",
  "phone": "555-1234",
  "items": [
    {"name": "Latte", "price": 3.5},
    {"name": "Bagel", "price": 1.75}
  ]
}
```

**Usage**
- Run with the default example file (falls back to `example_orders.json` if no argument):

```bash
python3 midterm_project.py
```

- Run with a specific file (e.g. a file your professor provides):

```bash
python3 midterm_project.py professor_orders.json
```

**Outputs**
- `customers.json`: JSON object mapping phone numbers to customer names. Example:

```json
{
  "555-1234": "Jane Doe",
  "555-5678": "John Smith"
}
```

- `items.json`: JSON object mapping item names to an object with `price` and `count`. Example:

```json
{
  "Latte": {"price": 3.5, "count": 12},
  "Bagel": {"price": 1.75, "count": 8}
}
```

---

File: `midterm_project.py`
