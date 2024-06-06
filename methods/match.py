from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.models import Match


class NewMatch(BaseModel):
    id: int
    first_team_id: int
    second_team_id: int
    first_team_score: int
    second_team_score: int


def get_all_matches(session: Session):
    return session.query(Match).all()


def create_match(session: Session, match: NewMatch):
    new_match = Match(
        first_team_id=match.first_team_id,
        second_team_id=match.second_team_id,
        first_team_score=match.first_team_score,
        second_team_score=match.second_team_score,
    )
    session.add(new_match)
    session.commit()
    return new_match
