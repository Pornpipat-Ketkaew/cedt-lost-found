from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict


class PostCreate(BaseModel):
    type: Literal["LOST", "FOUND"]
    title: str
    detail: str
    category: str
    place: str
    pickup_point: str | None = None
    secret_detail: str | None = None


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    type: str
    title: str
    detail: str
    category: str
    place: str
    pickup_point: str | None
    status: str
    created_at: datetime