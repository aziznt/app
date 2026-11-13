import json

with open("orders.json", encoding="utf-8") as f:
    orders = json.load(f)

for order in orders:
    customer = order.get("customer_name")
    items = order.get("items")
    total = sum([item['quantity']*item['price'] for item in items])
    print(f"{customer} - ${total}")