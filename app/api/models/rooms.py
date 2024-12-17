from sqlalchemy.orm import Mapped

from app.core.models.base import Base


class Rooms(Base):
    __tablename__ = 'rooms'

    room_number: Mapped[int]
    room_type: Mapped[str]
    price: Mapped[float]
    status: Mapped[str]
