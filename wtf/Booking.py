from sqlalchemy import Column, ForeignKey, String, DateTime

from urtaRent.models.db import Base


class Booking(Base):
    __tablename__ = "booking"

    id = Column(String, primary_key=True)
    tenant_form_id = Column(String, ForeignKey("tenant_form.id"))
    house_id = Column(String, ForeignKey("house.id"))
    checkin = Column(DateTime)
    checkout = Column(DateTime)
