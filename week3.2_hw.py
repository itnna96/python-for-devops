my_store = {
    'money': 100,
    'items': [
        {
            'name': 'apple',
            'amount': 3,
            'price': 5
        },
        {
            'name': 'orange',
            'amount': 1,
            'price': 10
        }
    ]
    }
def sell(store, selling_list):
    for sell_item in selling_list:
        for item in store['items']:
            if item['name'] == sell_item:
                if item['amount'] > 0:
                    item['amount'] -= 1
                    store['money'] += item['price']
                    print (f'Sell {item["name"]}. Money: {store["money"]}.')
                else:
                    print(f'No more {item["name"]} to sell.')
    return True
sell(my_store, ['apple', 'orange', 'orange'])
print(my_store)
