from sqlalchemy.orm import Session

from urtaApi import models, dto


def get_booking_by_tenant_form_id(db: Session, form_id: str):
    return db.query(models.Booking).filter(form_id == models.Booking.tenant_form_id).first()


def get_booking_by_house_id(db: Session, house_id: str):
    return db.query(models.Booking).filter(house_id == models.Booking.house_id).first()


def get_all_houses(db: Session):
    return db.query(models.House).all()


def get_house_by_id(db: Session, house_id: str):
    return db.query(models.House).filter(house_id == models.House.id).first()


def get_owner_by_id(db: Session, owner_id: str):
    return db.query(models.Owner).filter(owner_id == models.Owner.id).first()


def get_houses_by_owner_id(db: Session, owner_id: str):
    return db.query(models.House).filter(owner_id == models.House.owner_id).all()


def get_owner_by_house_id(db: Session, house_id: str):
    return get_owner_by_id(db.query(models.OwnerHouse).filter(house_id == models.House.id).first())  # pipipupu


def get_tenant_form_by_house_id(db: Session, house_id: str):
    return db.query(models.TenantForm).filter(house_id == models.TenantForm.house_id)


def get_tenant_form_by_id(db: Session, form_id: str):
    return db.query(models.TenantForm).filter(form_id == models.TenantForm.id)


def create_tenant_form(db: Session, tenant: dto.TenantForm):
    form = models.TenantForm(**tenant.model_dump())
    db.add(form)
    db.commit()
    db.refresh(form)


def create_house(db: Session, house: dto.House):
    h = models.House(**house.model_dump())
    db.add(h)
    db.commit()
    db.refresh(h)
    ho = models.OwnerHouse(house_id=house.id, owner_id=house.owner_id)
    db.add(ho)
    db.commit()
    db.refresh(ho)


def create_owner(db: Session, owner: dto.Owner):
    o = models.Owner(**owner.model_dump())
    db.add(o)
    db.commit()
    db.refresh(o)


def create_description(db: Session, description: dto.Description):
    des = models.Description(**description.model_dump())
    db.add(des)
    db.commit()
    db.refresh(des)
# idшники????
