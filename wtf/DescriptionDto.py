from pydantic import BaseModel
import BathroomTypeDto


class DescriptionDto(BaseModel):
    id: str
    bathroom_type: BathroomTypeDto
    towels: bool
    linen: bool
    furniture: list[str]
    barbecue_area: bool
    garage: bool
    house_area: float
    room_amount: int
    floor_amount: int
    appliances: list[str]
    utilities: list[str]

    class Config:
        from_attributes = True