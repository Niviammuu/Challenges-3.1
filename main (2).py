Write a function called  linear search product that takes the list of products and a target product name as input .the function should perform a linear search to find the target product in the List and return a list of indices of all occurrences of the product if found,or an empty list of the product if not found ￼Not
Certainly! Here's a Python function called `linear_search_product` that performs a linear search to find all occurrences of a target product name in a list of products and returns a list of indices:

```python
def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
```

You can use this function by passing your list of products and the target product name as arguments. It will return a list of indices where the target product is found, or an empty list if it's not found in the product list.