from sqlalchemy import Column, Integer, String
from app.db.database import Base
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    client_name = Column(String(60), nullable=False, unique=True)
    attendant_name = Column(String(60), nullable=False)
    audio_name = Column(String(255), nullable=False)