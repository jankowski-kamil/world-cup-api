from fastapi import FastAPI
from routers.team import router as team_router
from routers.match import router as match_router
from routers.table import router as table_router

app = FastAPI()

app.include_router(team_router)
app.include_router(match_router)
app.include_router(table_router)
