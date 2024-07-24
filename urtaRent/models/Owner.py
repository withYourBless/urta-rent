from sqlalchemy import Column, String

from urtaRent.repositiries.db import Base


class Owner(Base):
    __tablename__ = "owner"

    id = Column(String, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    telegram = Column(String)
