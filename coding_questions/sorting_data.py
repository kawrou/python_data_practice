# You are given a list of dictionaries, where each dictionary represents a product with the following keys:

# "name": A string representing the product's name.
# "price": An integer representing the price of the product.
# Write a function that:
# 
# Sorts the list of products by their price in ascending order.
# If two products have the same price, they should be sorted by their name in lexicographical order.


from typing import List


sample_data = [
    [
        {"name": "apple", "price": 50},
        {"name": "banana", "price": 30},
        {"name": "orange", "price": 50},
        {"name": "grape", "price": 30}
    ],
    [
        {"name": "apple", "price": 50}
    ],
    [
        {"name": "apple", "price": 30}, 
        {"name": "apple", "price": 50}
    ],
    [
        {"name": "banana", "price": 50},
        {"name": "apple", "price": 50}, 
    ]
]

def sort_data_by_price(data: List) -> List:
    return sorted(data, key=lambda x : (x["price"], x["name"]))

def main(data):
    sorted_data = sort_data_by_price(data)
    print(sorted_data)
    
if __name__ == "__main__":
    for data in sample_data:
        main(data)
