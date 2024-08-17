import uuid

from fastapi import APIRouter

from urtaApi import dto, repositories
from urtaApi.deps import SessionDep

router = APIRouter()


@router.post("/", tags=["tenant_form"])
async def create_tenant_form(form: dto.TenantFormIn, db: SessionDep):
    repositories.create_tenant_form(db, form, id=str(uuid.uuid4()))
