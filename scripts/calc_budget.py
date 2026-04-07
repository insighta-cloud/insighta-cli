import csv

total = 0
with open('output/order.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        qty = float(row['quantity'])
        if qty <= 0:
            continue
        price = float(row['price'])
        rate = float(row['rate']) if row['rate'].strip() else 155.0
        total += qty * price * rate

print(int(total))
