from config.__init__ import CURSOR, CONN

class Ingredient:
    all = {}

    def __init__(self, name, ingredient_id=None):
        self.ingredient_id = ingredient_id
        self.name = name

    def __repr__(self):
        return f"Ingredient(id={self.ingredient_id}, name='{self.name}')"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
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
        sql = "INSERT INTO ingredients (name) VALUES (?);"
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.ingredient_id = CURSOR.lastrowid
        type(self).all[self.ingredient_id] = self

    @classmethod
    def create(cls, name):
        ingredient = cls(name)
        ingredient.save()
        return ingredient

    def update(self):
        sql = "UPDATE ingredients SET name = ? WHERE id = ?;"
        CURSOR.execute(sql, (self.name, self.ingredient_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM ingredients WHERE id = ?;"
        CURSOR.execute(sql, (self.ingredient_id,))
        CONN.commit()
        del type(self).all[self.ingredient_id]
        self.ingredient_id = None

    @classmethod
    def instance_from_db(cls, row):
        ingredient = cls.all.get(row[0])
        if ingredient:
            ingredient.ingredient_id = row[0]
            ingredient.name = row[1]
        else:
            ingredient = cls(row[1], ingredient_id=row[0])
            cls.all[ingredient.ingredient_id] = ingredient
        return ingredient

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM ingredients;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
