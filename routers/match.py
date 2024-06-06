from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from methods.match import get_all_matches, create_match, NewMatch
from database.models import Match

router = APIRouter()


@router.get("/matches", response_model=list[Match], tags=["match"])
async def get_matches(db: Session = Depends(get_db)):
    teams = get_all_matches(db)
    return teams


@router.post("/matches", response_model=Match, tags=["match"])
async def get_matches(match: NewMatch, db: Session = Depends(get_db)):
    teams = create_match(db, match)
    return teams
