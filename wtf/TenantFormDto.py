from datetime import date

from pydantic import BaseModel

from urtaRent.dto import CommunicationMethodDto


class TenantFormDto(BaseModel):
    id: str
    house_id: int
    name: str
    phone_number: str
    communication_method: CommunicationMethodDto = "PHONE"
    guest_number: int
    checkin: date
    checkout: date
    comment: str

    class Config:
        from_attributes = True