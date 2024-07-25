import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from urtaApi import dto, models, repositories
from urtaApi.db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/house", response_model=list[dto.House])
async def get_all_houses(db: Session = Depends(get_db)):
    return repositories.get_all_houses(db)


@app.get("/house/{id}", response_model=dto.House)
async def get_house_by_id(house_id: str, db: Session = Depends(get_db)):
    return repositories.get_house_by_id(db, house_id)


@app.get("/owner/{id}", response_model=dto.Owner)
async def get_owner_by_id(owner_id: str, db: Session = Depends(get_db)):
    return repositories.get_owner_by_id(db, owner_id)


@app.post("/tenant_form")
async def create_tenant_form(form: dto.TenantForm, db: Session = Depends(get_db)):
    repositories.create_tenant_form(db, form)


@app.post("/house")
async def creaete_house(house: dto.House, db: Session = Depends(get_db)):
    repositories.create_house(db, house)


@app.post("/owner")
async def creaete_owner(owner: dto.Owner, db: Session = Depends(get_db)):
    repositories.create_owner(db, owner)


@app.post("/decription")
async def creaete_description(description: dto.Description, db: Session = Depends(get_db)):
    repositories.create_description(db, description)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)