from config import CURSOR, CONN

class Recipe:
    all = {}

    def __init__(self, name, user_id, id=None):
        self.id = id
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"Recipe(id={self.id}, name='{self.name}', user_id={self.user_id})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS recipes;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO recipes (name, user_id)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, user_id):
        recipe = cls(name, user_id)
        recipe.save()
        return recipe

    def update(self):
        sql = """
            UPDATE recipes
            SET name = ?, user_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.user_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM recipes WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        recipe = cls.all.get(row[0])
        if recipe:
            recipe.name = row[1]
            recipe.user_id = row[2]
        else:
            recipe = cls(row[1], row[2])
            recipe.id = row[0]
            cls.all[recipe.id] = recipe
        return recipe

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM recipes;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM recipes WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
