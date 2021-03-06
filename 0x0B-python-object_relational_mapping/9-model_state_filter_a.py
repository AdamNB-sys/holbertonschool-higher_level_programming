#!/usr/bin/python3
"""lists all State objects from the hbtn_0e_6_usa database
with an 'a' in their name"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()
    for state in Session.query(State).order_by(State.id.asc()).all():
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    Session.close()
