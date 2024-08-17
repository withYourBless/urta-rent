import uuid

from fastapi import APIRouter

from urtaApi import dto, repositories
from urtaApi.deps import SessionDep

router = APIRouter()


@router.get("/{id}", response_model=dto.Owner)
async def get_owner_by_id(owner_id: str, db: SessionDep):
    return repositories.get_owner_by_id(db, owner_id)


@router.post("/", tags=["owner"])
async def creaete_owner(owner: dto.OwnerIn, db: SessionDep):
    repositories.create_owner(db, owner, id=str(uuid.uuid4()))
