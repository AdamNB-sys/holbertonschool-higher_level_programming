#!/usr/bin/python3
"""adds a state object to the hbtn_0e_6_usa database"""


from unicodedata import name


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

    new_state = State(name='Louisiana')
    Session.add(new_state)
    Session.commit()
    print(new_state.id)
    Session.close()
