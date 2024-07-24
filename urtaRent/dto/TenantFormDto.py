from datetime import date

from pydantic import BaseModel
import CommunicationMethod


class TenantForm(BaseModel):
    id: str
    house_id: int
    name: str
    phone_number: str
    communication_method: CommunicationMethod = "PHONE"
    guest_number: int
    checkin: date
    checkout: date
    comment: str
