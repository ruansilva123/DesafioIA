from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    client_name = Column(String(60), nullable=False, unique=True)
    attendant_name = Column(String(60), nullable=False)
    payment_method = Column(String(60), nullable=False)
    effected = Column(Boolean, nullable=False)
    audio_name = Column(String(255), nullable=False)
    id_ata = Column(Integer, ForeignKey("atas.id"))

    ata = relationship("Ata", back_populates="calls")
    