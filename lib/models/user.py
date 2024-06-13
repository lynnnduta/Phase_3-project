from config.__init__ import CURSOR, CONN

class User:
    all = {}

    def __init__(self, username, email, user_id=None):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(id={self.user_id}, username='{self.username}', email='{self.email}')"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
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
        sql = "INSERT INTO users (username, email) VALUES (?, ?);"
        CURSOR.execute(sql, (self.username, self.email))
        CONN.commit()
        self.user_id = CURSOR.lastrowid
        type(self).all[self.user_id] = self

    @classmethod
    def create(cls, username, email):
        user = cls(username, email)
        user.save()
        return user

    def update(self):
        sql = "UPDATE users SET username = ?, email = ? WHERE id = ?;"
        CURSOR.execute(sql, (self.username, self.email, self.user_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM users WHERE id = ?;"
        CURSOR.execute(sql, (self.user_id,))
        CONN.commit()
        del type(self).all[self.user_id]
        self.user_id = None

    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user.user_id = row[0]
            user.username = row[1]
            user.email = row[2]
        else:
            user = cls(row[1], row[2], user_id=row[0])
            cls.all[user.user_id] = user
        return user

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM users;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
