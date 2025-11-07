import psycopg2


class Db:
    def __init__(self):
        self._connection = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "Maravaludi1.",
            database = "third_oop_test")

