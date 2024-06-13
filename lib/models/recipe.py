from config.__init__ import CURSOR, CONN

class Recipe:
    all = {}

    def __init__(self, name, user_id, recipe_id=None):
        self.recipe_id = recipe_id
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"Recipe(id={self.recipe_id}, name='{self.name}', user_id={self.user_id})"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
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
        sql = "INSERT INTO recipes (name, user_id) VALUES (?, ?);"
        CURSOR.execute(sql, (self.name, self.user_id))
        CONN.commit()
        self.recipe_id = CURSOR.lastrowid
        type(self).all[self.recipe_id] = self

    @classmethod
    def create(cls, name, user_id):
        recipe = cls(name, user_id)
        recipe.save()
        return recipe

    def update(self):
        sql = "UPDATE recipes SET name = ?, user_id = ? WHERE id = ?;"
        CURSOR.execute(sql, (self.name, self.user_id, self.recipe_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM recipes WHERE id = ?;"
        CURSOR.execute(sql, (self.recipe_id,))
        CONN.commit()
        del type(self).all[self.recipe_id]
        self.recipe_id = None

    @classmethod
    def instance_from_db(cls, row):
        recipe = cls.all.get(row[0])
        if recipe:
            recipe.recipe_id = row[0]
            recipe.name = row[1]
            recipe.user_id = row[2]
        else:
            recipe = cls(row[1], row[2], recipe_id=row[0])
            cls.all[recipe.recipe_id] = recipe
        return recipe

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM recipes;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
