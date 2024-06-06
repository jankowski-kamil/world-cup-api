from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class Base(DeclarativeBase, MappedAsDataclass):
    pass


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    first_team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    second_team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    first_team_score: Mapped[int]
    second_team_score: Mapped[int]


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(30))
