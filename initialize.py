from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy import JSON
# http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    # data = Column(Text, nullable=False)
    data = Column(JSON)


engine = create_engine('postgresql://tweetsql:tweetsql@tweetsql.cggizg1efi9f.us-east-1.rds.amazonaws.com/tweetsql')

Base.metadata.create_all(engine)