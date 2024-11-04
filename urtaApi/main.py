import uvicorn
import yaml
from fastapi import APIRouter, FastAPI

from urtaApi import models
from urtaApi.dsn import engine
from urtaApi.routes import login, owner, tenant_form, house

models.Base.metadata.create_all(bind=engine)

with open('config.yml') as f:
    app_config = yaml.safe_load(f)

api_router = FastAPI()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(owner.router, prefix="/owner", tags=["owner"])
api_router.include_router(tenant_form.router, prefix="/tenant_form")
api_router.include_router(house.router, prefix="/house", tags=["house"])

if __name__ == "__main__":
    uvicorn.run(api_router, host=app_config['app']['host'], port=app_config['app']['port'])
