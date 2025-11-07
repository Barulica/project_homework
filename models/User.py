from models.Db import Db


class User(Db):
    def __init__(self):
        super().__init__()
        self.__age = None
        self.__name = None
        self.__first_name = None
        self.__last_name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Age has to be at least 18")
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        split_name = name.split()

        if len(split_name) < 2:
            raise ValueError("Name has to be in 'First Last' format!")
        self.__first_name = split_name[0]
        self.__last_name = split_name[1]
        self.__name = name

    def add_user(self):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (first_name,last_name, age) VALUES (%s,%s, %s)", (self.__first_name, self.__last_name, self.__age))
        self._connection.commit()
        cursor.close()

    def show_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        self._connection.commit()
        cursor.close()

        return result