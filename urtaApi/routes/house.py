import uuid

from fastapi import APIRouter

from urtaApi import dto, repositories
from urtaApi.deps import SessionDep

router = APIRouter()


@router.get("/", response_model=list[dto.House])
async def get_all_houses(db: SessionDep):
    return repositories.get_all_houses(db)


@router.get("/{id}", response_model=dto.House)
async def get_house_by_id(house_id: str, db: SessionDep):
    return repositories.get_house_by_id(db, house_id)


@router.post("/")
async def creaete_house(house: dto.HouseIn, db: SessionDep):
    repositories.create_house(db, house, id=str(uuid.uuid4()))


@router.post("/", tags=["house"])
async def creaete_description(description: dto.DescriptionIn, db: SessionDep):
    repositories.create_description(db, description, id=str(uuid.uuid4()))
