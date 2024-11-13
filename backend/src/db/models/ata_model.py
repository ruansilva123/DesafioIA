from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Ata(Base):
    __tablename__ = "atas"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name_ata = Column(String(30), nullable=False, unique=True)

    calls = relationship("Call", back_populates="ata")