from pydantic import BaseModel, field_validator,model_validator, computed_field 



class User(BaseModel):
    user_name: str 


    @field_validator("user_name")
    def validate_user_name(cls, value):
        if len(value) < 4:
            raise ValueError("user_name must be at least 4 characters long")
        return value 
    

class Signup(BaseModel):
    password: str 
    confirm_password: str 

    @model_validator(mode="after")
    def check_password(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("password and confirm_password must match")
        return values 

class Product(BaseModel):
    price: float 
    quantity: int 

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity 
    




# correct data 
# print(User(user_name="JohnDoe"))

# incorrect Data 
# print(User(user_name="JD")) 


# correct singup data
# print(Signup(password="password123", confirm_password="password123"))

# incorrect signup data
# print(Signup(password="password123",confirm_password="password"))


print(Product(price=100.00, quantity=5).total_price)