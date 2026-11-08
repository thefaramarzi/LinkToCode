from sqlalchemy import Column , Integer ,String ,DateTime,URL
from sqlalchemy.sql import func
from db import Base ,engine



class LinkToCode (Base):
    __tablename__ = "links"
    id = Column(Integer,primary_key=True,index=True)

    long_link = Column(String,unique=True,nullable=False)
    short_code = Column(String,unique=True,nullable=False)
    Number_of_views = Column(Integer,default=0)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

Base.metadata.create_all(engine)    

