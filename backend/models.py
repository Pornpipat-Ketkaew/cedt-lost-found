from datetime import datetime
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(5))
    title: Mapped[str] = mapped_column(String(100))
    detail: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(30))
    place: Mapped[str] = mapped_column(String(100))
    pickup_point: Mapped[str | None] = mapped_column(String(100))
    secret_detail: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(10), default="open")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())