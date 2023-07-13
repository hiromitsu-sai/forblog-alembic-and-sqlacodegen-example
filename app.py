from sqlalchemy import select

from models import Address, User
from session import Session

with Session() as session:
    # query for ``User`` objects
    statement1 = select(User).filter_by(name="ed")
    # list of ``User`` objects
    user_obj = session.scalars(statement1).all()
    print(user_obj[0].__repr__)

    # query for individual columns
    statement2 = select(User.name, User.fullname)
    # list of Row objects
    rows = session.execute(statement2).all()
    print(rows[0].name, rows[0].fullname)
