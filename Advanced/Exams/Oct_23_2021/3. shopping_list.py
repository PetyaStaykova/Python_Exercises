def shopping_list(budget: int, **kwargs):
    if budget < 100:
        return f'You do not have enough budget.'
    bought_items = {}

    for product, price in kwargs.items():
        product_price = price[0] * price[1]
        if product_price <= budget:

            budget -= product_price
            if product not in bought_items:
                bought_items[product] = product_price
            else:
                bought_items[product] += product_price
            if len(bought_items) == 5:
                break

    return '\n'.join([f'You bought {product} for {product_price:.2f} leva.' for product, product_price in bought_items.items()])


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))
print(shopping_list(20, jeans=(19.99, 1),))
print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5), \
                    tomatoes=(4.20, 1), milk=(2.50, 2), juice=(2, 3), eggs=(3, 1),))
