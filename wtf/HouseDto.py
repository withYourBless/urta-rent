from pydantic import BaseModel


class HouseDto(BaseModel):
    id: str
    description_id: str
    title: str
    price: int
    max_capacity: int
    address: str
    availability: bool = True
    photos: list[str]

    class Config:
        from_attributes = True