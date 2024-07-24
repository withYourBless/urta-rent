from pydantic import BaseModel
import BathroomType


class Description(BaseModel):
    id: str
    bathroom_type: BathroomType
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