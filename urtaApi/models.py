import enum
from sqlalchemy import Column, ForeignKey, String, DateTime, Integer, Boolean, ARRAY, Float, Enum
from sqlalchemy.orm import relationship

from urtaApi.dsn import Base
from urtaApi.dto import BathroomType, CommunicationMethod


class Booking(Base):
    __tablename__ = "booking"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    tenant_form_id = Column(String, ForeignKey("tenant_form.id"))
    house_id = Column(String, ForeignKey("house.id"))
    checkin = Column(DateTime)
    checkout = Column(DateTime)


class Description(Base):
    __tablename__ = "description"
    __table_args__ = {'extend_existing': True}

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


class House(Base):
    __tablename__ = "house"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    owner_id = Column(String, ForeignKey("owner.id"))
    description_id = Column(String, ForeignKey("description.id"))
    title = Column(String)
    price = Column(Integer)
    max_capacity = Column(Integer)
    address = Column(String)
    availability = Column(Boolean)
    photos = Column(ARRAY(String))
    owner = relationship("Owner", back_populates="houses")


class Owner(Base):
    __tablename__ = "owner"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    telegram = Column(String)
    houses = relationship("House", back_populates="owner")
    role = Column(String, default="user")
    password = Column(String)


class TenantForm(Base):
    __tablename__ = "tenant_form"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    house_id = Column(String, ForeignKey("house.id"))
    name = Column(String)
    phone_number = Column(String)
    communication_method = Column(Enum(CommunicationMethod), default=CommunicationMethod.PHONE)
    guest_number = Column(Integer)
    checkin = Column(DateTime)
    checkout = Column(DateTime)
    comment = Column(String)


class OwnerHouse(Base):
    __tablename__ = "owner_house"
    __table_args__ = {'extend_existing': True}

    house_id = Column(String, primary_key=True)
    owner_id = Column(String, ForeignKey("owner.id"))
