import sqlite3


class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS "User" (
                "id"	INTEGER,
                "name"	TEXT,
                "surname" TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
            """
        )

    def create_user(self, name,surname):
        self.cur.execute(
            """INSERT INTO User(name,surname) VALUES (?,?)""",
            (name, surname)

        )
        self.conn.commit()


    def get_users(self):
        self.cur.execute(
            """SELECT * FROM User"""
        )
        user = dict_fetchall(self.cur)
        return user


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
