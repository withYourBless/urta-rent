from datetime import date

from pydantic import BaseModel


class Booking(BaseModel):
    id: str
    tenant_form_id: str
    house_id: str
    checkin: date
    checkout: date