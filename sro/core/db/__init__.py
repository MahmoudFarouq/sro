import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)

def session(session_instance: Session):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                session_instance.commit()
            except:
                session_instance.rollback()
                raise
            finally:
                session_instance.close()
        return inner_wrapper
    return outer_wrapper