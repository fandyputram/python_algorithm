# Integer Ascending
numbers = [5, 2, 9, 1, 5]
sorted_numbers = sorted(numbers)
print("Integer Ascending:", sorted_numbers)

# Integer Descending
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Integer Descending:", sorted_numbers_desc)

# String Ascending
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_words = sorted(words)
print("String Ascending:", sorted_words)

# String Descending
sorted_words_desc = sorted(words, reverse=True)
print("String Descending:", sorted_words_desc)

# Struct Ascending (Rating, then Price)
products = [
    {"name": "Apple", "rating": 4, "price": 2.5},
    {"name": "Banana", "rating": 3, "price": 1.5},
    {"name": "Cherry", "rating": 5, "price": 3.0}
]
sorted_products = sorted(products, key=lambda x: (x["rating"], x["price"]))
print("Struct Ascending (Rating, then Price):")
for product in sorted_products:
    print(product)

# Struct Descending (Rating, then Price)
sorted_products_desc = sorted(products, key=lambda x: (x["rating"], x["price"]), reverse=True)
print("Struct Descending (Rating, then Price):")
for product in sorted_products_desc:
    print(product)
