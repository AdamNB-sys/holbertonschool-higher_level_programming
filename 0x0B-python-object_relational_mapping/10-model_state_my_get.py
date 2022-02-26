#!/usr/bin/python3
"""lists first State object in the hbtn_0e_6_usa database"""


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
    state_id = Session.query(State).filter(State.name == argv[4]).first()

    if state_id:
        print(state_id.id)
    else:
        print('Not found')
    Session.close()
