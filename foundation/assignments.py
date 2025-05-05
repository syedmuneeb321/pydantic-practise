from pydantic import BaseModel


class Product(BaseModel):
    id: int 
    name: str 
    price: float 
    in_stock: bool = True  # default value for in_stock is True



product_dict = {
    "id":1,
    "name": "laptop",
    "price": 1000.00,
    "in_stock": True
}

product = Product(**product_dict)
print(product)

# intentionally incorrect data
# product_dict_w = {
#     "id": "1a", # incorrect type
#     "name": "laptop",
#     "price": "1000.00",  # incorrect type
#     "in_stock": True
# }

# wrong_product = Product(**product_dict_w)
# print(wrong_product)