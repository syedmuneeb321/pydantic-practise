from pydantic import BaseModel,computed_field, Field  


class Booking(BaseModel):
    user_id: int 
    room_id: int 
    nights: int = Field(..., ge=1)
    rate_per_night: float 

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night 
    




# Example of correct data
booking_data = Booking(user_id=1, room_id=101, nights=3, rate_per_night=100.0)
print(booking_data)
print("Total Cost:", booking_data.total_cost)

