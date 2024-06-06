from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Team


def get_all_teams(session: Session):
    return session.query(Team).all()


def create_team(session: Session, team_name: str):
    team = Team(name=team_name)
    session.add(team)
    session.commit()
    return team
