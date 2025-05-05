from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional 



class Lesson(BaseModel):
    lesson_id: int
    topic: str 


class Module(BaseModel):
    module_id: int
    name: str 
    lessons: List[Lesson]  

class Course(BaseModel):
    course_id: int 
    title: str 
    modules: List[Module]



lessons = [
    Lesson(lesson_id=1, topic="Introduction to Python"),
    Lesson(lesson_id=2, topic="Data Structures"),
    Lesson(lesson_id=3, topic="Object-Oriented Programming"),
]

module = Module(
    module_id=1,
    name="python_basics",
    lessons=lessons

)

course = Course(
    course_id = 101,
    title = "python programming",
    modules = [module]
)

# print(course)


############################# second example #############################

class Address(BaseModel):
    street: str 
    city: str 
    state: str 
    zip_code: str 

class User(BaseModel):
    user_id: int 
    name: str = Field(..., min_length=1, max_length=50) 
    email: EmailStr
    address: Address


class Comment(BaseModel):
    comment_id: int 
    user_id: int 
    content: str = Field(..., min_length=1, max_length=500)  # content must be between 1 and 500 characters long
    timestamp: str  # ISO 8601 format (e.g., "2023-10-01T12:00:00Z")
    replies: List['Comment'] = []  # Recursive type for nested comments

Comment.model_rebuild()



example_address = Address(
    street="123 Main St",
    city="Springfield",
    state="IL",
    zip_code="62701"
)

example_user = User(
    user_id = 101,
    name="John Doe",
    email="johndoe123@gmail.com",
    address=example_address
)

comment = Comment(
    comment_id=1,
    user_id=example_user.user_id,
    content="This is a comment.",
    timestamp="2023-10-01T12:00:00Z",
    replies=[
        Comment(
            comment_id=2,
            user_id=example_user.user_id,
            content="This is a reply.",
            timestamp="2023-10-01T12:05:00Z",
        )
    ]
)


print(comment)