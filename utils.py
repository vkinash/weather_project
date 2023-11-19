from database import SessionLocal


class DBConnect:
    def __init__(self, session=SessionLocal()):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, *args, **kwargs):
        self.session.close()
