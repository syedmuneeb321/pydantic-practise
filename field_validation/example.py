from pydantic import BaseModel
from typing import List, Optional, Dict 



class Cart(BaseModel):
    user_id: int 
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str 
    content: str 
    image_url: Optional[str] = None 





cart_dict = {
    "user_id": 1,
    "items": ["apple", "banana", "orange"],
    "quantities": {
        "apple": 2,
        "banana": 3,
        "orange": 1
    }
}

cart_data = Cart(**cart_dict)
print(cart_data)


blog_post_dict = {
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "image_url": "http://example.com/image.jpg"
}

blog_post_data = BlogPost(**blog_post_dict)
print(blog_post_data)
