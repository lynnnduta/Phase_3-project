import re
from config import CURSOR, CONN

class User:
    all = {}

    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty")
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', value):
            raise ValueError("Invalid email address")
        self._email = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT UNIQUE
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS users;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO users (username, email)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.username, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, username, email):
        user = cls(username, email)
        user.save()
        return user

    def update(self):
        sql = """
            UPDATE users
            SET username = ?, email = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.username, self.email, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM users WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user.username = row[1]
            user.email = row[2]
        else:
            user = cls(row[1], row[2])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM users;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM users WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
