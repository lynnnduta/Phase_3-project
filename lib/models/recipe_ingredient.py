from config.__init__ import CURSOR, CONN

class RecipeIngredient:
    all = {}

    def __init__(self, recipe_id, ingredient_id, quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity

    def __repr__(self):
        return f"RecipeIngredient(recipe_id={self.recipe_id}, ingredient_id={self.ingredient_id}, quantity={self.quantity})"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS recipe_ingredients (
                recipe_id INTEGER,
                ingredient_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (recipe_id) REFERENCES recipes(id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
                PRIMARY KEY (recipe_id, ingredient_id)
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
        sql = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?);"
        CURSOR.execute(sql, (self.recipe_id, self.ingredient_id, self.quantity))
        CONN.commit()
        type(self).all[(self.recipe_id, self.ingredient_id)] = self

    @classmethod
    def create(cls, recipe_id, ingredient_id, quantity):
        recipe_ingredient = cls(recipe_id, ingredient_id, quantity)
        recipe_ingredient.save()
        return recipe_ingredient

    def update(self):
        sql = "UPDATE recipe_ingredients SET quantity = ? WHERE recipe_id = ? AND ingredient_id = ?;"
        CURSOR.execute(sql, (self.quantity, self.recipe_id, self.ingredient_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM recipe_ingredients WHERE recipe_id = ? AND ingredient_id = ?;"
        CURSOR.execute(sql, (self.recipe_id, self.ingredient_id))
        CONN.commit()
        del type(self).all[(self.recipe_id, self.ingredient_id)]

    @classmethod
    def instance_from_db(cls, row):
        recipe_ingredient = cls.all.get((row[0], row[1]))
        if recipe_ingredient:
            recipe_ingredient.recipe_id = row[0]
            recipe_ingredient.ingredient_id = row[1]
            recipe_ingredient.quantity = row[2]
        else:
            recipe_ingredient = cls(row[0], row[1], row[2])
            cls.all[(recipe_ingredient.recipe_id, recipe_ingredient.ingredient_id)] = recipe_ingredient
        return recipe_ingredient

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM recipe_ingredients;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
