from sqlmodel import SQLModel, Field
from typing import Optional


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    platform: str
    genre: str


class Listing(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    game_id: int = Field(foreign_key="game.id")
    user_id: int = Field(foreign_key="user.id")
    price: float


class Rental(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    listing_id: int = Field(foreign_key="listing.id")
    user_id: int = Field(foreign_key="user.id")


class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rental_id: int = Field(foreign_key="rental.id")
    amount: float