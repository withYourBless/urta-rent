from datetime import date
from enum import Enum

from pydantic import BaseModel


class BathroomType(str, Enum):
    BATH = "BATH"
    SHOWER = "SHOWER"


class Owner(BaseModel):
    id: str
    name: str
    phone_number: str
    telegram: str

    class Config:
        from_attributes = True


class Booking(BaseModel):
    id: str
    tenant_form_id: str
    house_id: str
    checkin: date
    checkout: date

    class Config:
        from_attributes = True


class CommunicationMethod(str, Enum):
    TELEGRAM = "TELEGRAM"
    PHONE = "PHONE"
    WHATSAPP = "WHATSAPP"


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

    class Config:
        from_attributes = True


class House(BaseModel):
    id: str
    owner_id: str
    description_id: str
    title: str
    price: int
    max_capacity: int
    address: str
    availability: bool = True
    photos: list[str]

    class Config:
        from_attributes = True


class TenantForm(BaseModel):
    id: str
    house_id: int
    name: str
    phone_number: str
    communication_method: CommunicationMethod = 'PHONE'
    guest_number: int
    checkin: date
    checkout: date
    comment: str

    class Config:
        from_attributes = True
