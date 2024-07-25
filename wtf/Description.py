from sqlalchemy import Boolean, Column, Integer, String, ARRAY, Enum, Float

from urtaRent.models.db import Base
from BathroomType import BathroomType


class Description(Base):
    __tablename__ = "description"

    id = Column(String, primary_key=True)
    bathroom_type = Column(Enum(BathroomType))
    towels = Column(Boolean)
    linen = Column(Boolean)
    furniture = Column(ARRAY(String))
    barbecue_area = Column(Boolean)
    garage = Column(Boolean)
    house_area = Column(Float)
    room_amount = Column(Integer)
    floor_amount = Column(Integer)
    appliances = Column(ARRAY(String))
    utilities = Column(ARRAY(String))