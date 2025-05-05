from pydantic import BaseModel, Field 
from typing import Optional

class Employee(BaseModel):
    id: int 
    name: str = Field(..., min_length=3, max_length=50,description="Name of the employee",example="John Doe") 
    age: int = Field(..., gt=18, le=70, description="Age of the employee", example=30)
    department: Optional[str] = "General" 
    salary: float = Field(..., ge = 10000)



employee_data = Employee(
    id=1,
    name="John Doe",
    age=30,
    department="HR",
    salary=50000.0
)

print(employee_data)


# Example of incorrect data
employee_data_invalid = Employee(
    id=2, 
    name="JD",
    age=17,  # Invalid age
    department="IT",
    salary=8000.0  # Invalid salary
)


print(employee_data_invalid)