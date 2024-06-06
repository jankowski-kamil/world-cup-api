from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Team
from methods.team import get_all_teams, create_team

router = APIRouter()


@router.get("/teams", response_model=list[Team], tags=["team"])
async def get_teams(db: Session = Depends(get_db)):
    teams = get_all_teams(db)
    return teams


@router.post("/teams", response_model=Team, tags=["team"])
async def get_teams(team_name: str, db: Session = Depends(get_db)):
    team = create_team(db, team_name)
    return team
