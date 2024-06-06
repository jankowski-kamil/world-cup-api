from sqlalchemy import case, func
from sqlalchemy.orm import Session
from database.models import Team, Match
from enums.enums import SortType


def get_table_teams(
    session: Session,
    limit: int = 4,
    sort: SortType = SortType.asc,
    from_points: int | None = 0,
    to_points: int | None = 10,
):
    points_first_team = case(
        (Match.first_team_score > Match.second_team_score, 3),
        (Match.first_team_score == Match.second_team_score, 1),
        (Match.first_team_score < Match.second_team_score, 0),
    )

    points_second_team = case(
        (Match.second_team_score > Match.first_team_score, 3),
        (Match.second_team_score == Match.first_team_score, 1),
        (Match.second_team_score < Match.first_team_score, 0),
    )

    first_team_points = (
        session.query(
            Team.name.label("team_name"),
            func.sum(points_first_team).label("team_points"),
        )
        .join(Match, Team.id == Match.first_team_id)
        .group_by(Team.name)
    )

    second_team_points = (
        session.query(
            Team.name.label("team_name"),
            func.sum(points_second_team).label("team_points"),
        )
        .join(Match, Team.id == Match.second_team_id)
        .group_by(Team.name)
    )

    total_points = first_team_points.union_all(second_team_points).subquery()

    if sort == SortType.asc:
        sort_by = func.sum(total_points.c.team_points).asc()
    else:
        sort_by = func.sum(total_points.c.team_points).desc()

    return (
        session.query(
            total_points.c.team_name.label("name"),
            func.sum(total_points.c.team_points).label("total_points"),
        )
        .group_by(total_points.c.team_name)
        .having(func.sum(total_points.c.team_points).between(from_points, to_points))
        .order_by(sort_by)
        .limit(limit)
        .all()
    )
