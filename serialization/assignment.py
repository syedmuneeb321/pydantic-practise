from pydantic import BaseModel, Field, EmailStr , ConfigDict
from datetime import datetime,timezone
from typing import List, Optional 




class Address(BaseModel):
    street: str 
    city: str 
    state: str 
    zip_code: str 

class User(BaseModel):
    user_id: int
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    created_at: datetime 
    is_active: bool = True 
    address: Address 
    tags: Optional[List[str]] = None 

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

user_data = User(
    user_id=1,
    name="John Doe",
    email="johndoe123@gmail.com",
    created_at  = datetime(2024,1,2, 12,23),
    address=Address(
        street="123 Main St",
        city="New York",
        state="NY",
        zip_code="10001"
    ),
    tags=["admin", "user"]

)


# print(datetime.now(timezone.utc)) 

# user in dict format 
print(user_data.model_dump())


print("=="*20)

print(user_data.model_dump_json(indent=4))


# model config using json_encoders for datetime and other types