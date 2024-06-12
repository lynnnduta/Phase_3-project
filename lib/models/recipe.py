from config.__init__ import CURSOR, CONN

class Recipe:
    all = {}

    def __init__(self, name, instructions, user_id, id=None):
        self.id = id
        self.name = name
        self.instructions = instructions
        self.user_id = user_id

    def __repr__(self):
        return f"Recipe(id={self.id}, name='{self.name}', instructions='{self.instructions}', user_id={self.user_id})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, value):
        if not value:
            raise ValueError("Instructions cannot be empty")
        self._instructions = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                instructions TEXT,
                user_id INTEGER,
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
        sql = """
            INSERT INTO recipes (name, instructions, user_id)
            VALUES (?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.instructions, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, instructions, user_id):
        recipe = cls(name, instructions, user_id)
        recipe.save()
        return recipe
