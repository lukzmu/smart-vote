from uuid import uuid4

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime,
    Float,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description = Column(String)
    public_key = Column(String)
    private_key = Column(String)
    vote = Column(UUID, ForeignKey("votes.id"))


class Vote(Base):
    __tablename__ = 'votes'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    category = Column(String)
    description = Column(String)
    image = Column(String)
    is_active = Column(Boolean)
    answers = relationship("Answer")
