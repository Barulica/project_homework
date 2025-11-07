from models.Db import Db



class User(Db):
    def __init__(self):
        super().__init__()
        print(self._connection)

toma = User("Toma")