from pydantic import BaseModel


class OwnerDto(BaseModel):
    id: str
    name: str
    phone_number: str
    telegram: str

    class Config:
        from_attributes = True