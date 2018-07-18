from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

# def Session():
#       from aldjemy.core import get_engine
#       engine = get_engine()
#       _Session =sessionmaker(bind=engine)
#       return _Session()
#
# session=Session()

engine = create_engine('mysql://root:password@localhost:3306/user_test',echo=False)

Session = sessionmaker(bind=engine)
session = Session()


