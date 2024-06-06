from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from methods.table import get_table_teams
from enums.enums import SortType, TableModel

router = APIRouter()


@router.get("/table", response_model=list[TableModel], tags=["table"])
async def get_table(
    from_points: int | None = 0,
    to_points: int | None = 10,
    limit: int = 4,
    sort: SortType = SortType.asc,
    db: Session = Depends(get_db),
):
    teams = get_table_teams(db, limit, sort, from_points, to_points)
    return teams
