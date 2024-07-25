from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY

from urtaRent.models.db import Base


class House(Base):
    __tablename__ = "house"

    id = Column(String, primary_key=True)
    description_id = Column(String, ForeignKey("description.id"))
    title = Column(String)
    price = Column(Integer)
    max_capacity = Column(Integer)
    address = Column(String)
    availability = Column(Boolean)
    photos = Column(ARRAY(String))