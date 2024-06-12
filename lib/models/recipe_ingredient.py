from config.__init__ import CURSOR, CONN

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
                FOREIGN KEY (recipe_id) REFERENCES recipes(id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
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
        recipeingredient = cls(recipe_id, ingredient_id)
        recipeingredient.save()
        return recipeingredient
