from pydantic import BaseModel


class Owner(BaseModel):
    id: str
    name: str
    phone_number: str
    telegram: str