from config import CURSOR, CONN

class RecipeIngredient:
    all = {}

    def __init__(self, recipe_id, ingredient_id, id=None):
        self.id = id
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id

    def __repr__(self):
        return f"RecipeIngredient(id={self.id}, recipe_id={self.recipe_id}, ingredient_id={self.ingredient_id})"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS recipe_ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_id INTEGER,
                ingredient_id INTEGER,
                FOREIGN KEY (recipe_id) REFERENCES recipes (id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS recipe_ingredients;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO recipe_ingredients (recipe_id, ingredient_id)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.recipe_id, self.ingredient_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, recipe_id, ingredient_id):
        recipe_ingredient = cls(recipe_id, ingredient_id)
        recipe_ingredient.save()
        return recipe_ingredient

    def update(self):
        sql = """
            UPDATE recipe_ingredients
            SET recipe_id = ?, ingredient_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.recipe_id, self.ingredient_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM recipe_ingredients WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        recipe_ingredient = cls.all.get(row[0])
        if recipe_ingredient:
            recipe_ingredient.recipe_id = row[1]
            recipe_ingredient.ingredient_id = row[2]
        else:
            recipe_ingredient = cls(row[1], row[2])
            recipe_ingredient.id = row[0]
            cls.all[recipe_ingredient.id] = recipe_ingredient
        return recipe_ingredient

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM recipe_ingredients;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM recipe_ingredients WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
