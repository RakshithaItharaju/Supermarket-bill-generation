import csv
import os
from datetime import datetime

DATA_FILE = os.path.join('data', 'products.csv')
RECEIPT_DIR = 'receipts'
TAX_RATE = 0.05
DISCOUNT_THRESHOLD = 2000.0
DISCOUNT_RATE = 0.02

def load_products(path=DATA_FILE):
    products = {}
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            code = row['code'].strip()
            products[code] = {
                'name': row['name'].strip(),
                'price': float(row['price']),
            }
    return products

def format_currency(v):
    return f"₹{v:,.2f}"

def create_receipt(bill_items, subtotal, tax, discount, total, customer_name='Customer'):
    if not os.path.exists(RECEIPT_DIR):
        os.makedirs(RECEIPT_DIR, exist_ok=True)
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(RECEIPT_DIR, f'receipt_{now}.txt')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Supermarket - Receipt\n')
        f.write('Generated on: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f.write('Customer: ' + customer_name + '\n')
        f.write('\n')
        f.write(f"{'Qty':>3}  {'Item':<30} {'Price':>10} {'Total':>12}\n")
        f.write('-'*60 + '\n')
        for item in bill_items:
            f.write(f"{item['qty']:>3}  {item['name']:<30} {format_currency(item['price']):>10} {format_currency(item['total']):>12}\n")
        f.write('-'*60 + '\n')
        f.write(f"{'Subtotal':>46}: {format_currency(subtotal):>12}\n")
        f.write(f"{'Tax (' + str(int(TAX_RATE*100)) + '%)':>46}: {format_currency(tax):>12}\n")
        f.write(f"{'Discount':>46}: {format_currency(discount):>12}\n")
        f.write(f"{'Total':>46}: {format_currency(total):>12}\n")
    return filename

def run_cli():
    products = load_products()
    print('Loaded', len(products), 'products.')
    customer = input('Enter customer name (or press Enter): ').strip() or 'Customer'
    bill_items = []
    while True:
        code = input('Enter product code (or "done"): ').strip()
        if code.lower() == 'done':
            break
        if code not in products:
            print('Product not found. Try again.')
            continue
        try:
            qty = float(input('Quantity: '))
        except ValueError:
            print('Invalid quantity.')
            continue
        item = products[code]
        total = item['price'] * qty
        bill_items.append({'code': code, 'name': item['name'], 'price': item['price'], 'qty': qty, 'total': total})
        print(f"Added: {item['name']} x {qty} = {format_currency(total)}")

    if not bill_items:
        print('No items added. Exiting.')
        return

    subtotal = sum(i['total'] for i in bill_items)
    tax = subtotal * TAX_RATE
    discount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_THRESHOLD else 0.0
    total = subtotal + tax - discount

    print('\n----- BILL SUMMARY -----')
    print(f'Subtotal: {format_currency(subtotal)}')
    print(f'Tax ({int(TAX_RATE*100)}%): {format_currency(tax)}')
    print(f'Discount: {format_currency(discount)}')
    print(f'Total: {format_currency(total)}')
    receipt_file = create_receipt(bill_items, subtotal, tax, discount, total, customer)
    print('Receipt saved to', receipt_file)

if __name__ == '__main__':
    run_cli()
