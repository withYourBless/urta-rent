from sqlalchemy import Column, ForeignKey, Integer, String, Enum, DateTime

from urtaRent.repositiries.db import Base
from urtaRent.models.CommunicationMethod import CommunicationMethod


class TenantForm(Base):
    __tablename__ = "tenant_form"

    id = Column(String, primary_key=True)
    house_id = Column(Integer, ForeignKey("house.id"))
    name = Column(String)
    phone_number = Column(String)
    communication_method = Column(Enum(CommunicationMethod))
    guest_number = Column(Integer)
    checkin = Column(DateTime)
    checkout = Column(DateTime)
    comment = Column(String)
