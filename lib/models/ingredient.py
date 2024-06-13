from config import CURSOR, CONN

class Ingredient:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Ingredient(id={self.id}, name='{self.name}')"

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
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS ingredients;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO ingredients (name)
            VALUES (?);
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        ingredient = cls(name)
        ingredient.save()
        return ingredient

    def update(self):
        sql = """
            UPDATE ingredients
            SET name = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM ingredients WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        ingredient = cls.all.get(row[0])
        if ingredient:
            ingredient.name = row[1]
        else:
            ingredient = cls(row[1])
            ingredient.id = row[0]
            cls.all[ingredient.id] = ingredient
        return ingredient

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM ingredients;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM ingredients WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
