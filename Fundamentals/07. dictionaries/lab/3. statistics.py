input_data = input()
products_in_stock = {}

while not input_data == "statistics":
    data_pairs = input_data.split(': ')
    product = data_pairs[0]
    quantity = int(data_pairs[1])
    if product not in products_in_stock:
        products_in_stock[product] = quantity
    else:
        products_in_stock[product] += quantity
    input_data = input()

print('Products in stock:')

for product, quantity in products_in_stock.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products_in_stock)}')
print(f'Total Quantity: {sum(products_in_stock.values())}')