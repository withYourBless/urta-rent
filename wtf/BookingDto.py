from datetime import date

from pydantic import BaseModel


class BookingDto(BaseModel):
    id: str
    tenant_form_id: str
    house_id: str
    checkin: date
    checkout: date

    class Config:
        from_attributes = True