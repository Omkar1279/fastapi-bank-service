from fastapi import FastAPI
from api.endpoints import banks, branches

app = FastAPI()

app.include_router(banks.router, prefix="/banks", tags=["banks"])
app.include_router(branches.router, prefix="/branches", tags=["branches"])
