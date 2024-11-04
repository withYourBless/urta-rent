import uuid

from psycopg2.extras import NamedTupleCursor

from sqlalchemy.orm import Session

from urtaApi import models, dto
from urtaApi.dsn import conn
from urtaApi.security import get_password_hash


def get_booking_by_tenant_form_id(db: Session, form_id: str):
    return db.query(models.Booking).filter(form_id == models.Booking.tenant_form_id).first()


def get_booking_by_house_id(db: Session, house_id: str):
    return db.query(models.Booking).filter(house_id == models.Booking.house_id).first()


def get_all_houses(db: Session):
    return db.query(models.House).all()


def get_house_by_id(db: Session, house_id: str):
    return db.get(models.House, house_id)


def get_owner_by_id(db: Session, owner_id: str):
    return db.get(models.Owner, owner_id)


def get_owner_by_phone_number(phone: str):
    curs = conn.cursor(cursor_factory=NamedTupleCursor)
    curs.execute("SELECT * FROM owner WHERE phone_number=%s", (phone,))
    owner = curs.fetchone()
    return owner


def get_houses_by_owner_id(db: Session, owner_id: str):
    return db.query(models.House).filter(owner_id == models.House.owner_id).all()


def get_owner_by_house_id(db: Session, house_id: str):
    return get_owner_by_id(db.query(models.OwnerHouse).filter(house_id == models.House.id).first())


def get_tenant_form_by_house_id(db: Session, house_id: str):
    return db.query(models.TenantForm).filter(house_id == models.TenantForm.house_id)


def get_tenant_form_by_id(db: Session, form_id: str):
    return db.query(models.TenantForm).filter(form_id == models.TenantForm.id)


def create_tenant_form(db: Session, tenant: dto.TenantFormIn, id: uuid):
    form = models.TenantForm(**tenant.model_dump(), id=id)
    db.add(form)
    db.commit()
    db.refresh(form)


def create_house(db: Session, house: dto.HouseIn, id: uuid):
    h = models.House(**house.model_dump(), id=id)
    db.add(h)
    db.commit()
    db.refresh(h)
    ho = models.OwnerHouse(house_id=id, owner_id=house.owner_id)
    db.add(ho)
    db.commit()
    db.refresh(ho)


def create_owner(db: Session, owner: dto.OwnerIn, id: uuid):
    o = models.Owner(**owner.model_dump(), id=id)
    o.password = get_password_hash(o.password)
    db.add(o)
    db.commit()
    db.refresh(o)


def create_description(db: Session, description: dto.DescriptionIn, id: uuid):
    des = models.Description(**description.model_dump(), id=id)
    db.add(des)
    db.commit()
    db.refresh(des)
