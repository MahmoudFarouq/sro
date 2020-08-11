import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)

def transaction(func):
    def wrapper(*args, **kwargs):
        try:
            session_instance = Session()
            kwargs['session'] = session_instance
            func(*args, **kwargs)
            session_instance.commit()
        except:
            session_instance.rollback()
            raise
        finally:
            session_instance.close()
    return wrapper