import sqlite3


class ProductUser:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()


    def initiate_db(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        """)
        self.connection.commit()


    def add_products(self):
        a = 1
        for i in range(4):
            self.cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f'Product {a}', f'описание {a}', f'{a*100}'))
            a += 1
            self.connection.commit()


    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Products")
        products = self.cursor.fetchall()

        self.connection.commit()
        return products

    def add_user(self, username, email, age):
        self.cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                           (f"{username}", f"{email}", f"{age}", f"{1000}"))
        self.connection.commit()

    def is_included(self, username):
        check_users = self.cursor.execute(f"SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
        self.connection.commit()
        if check_users is None:
            return False
        else:
            return True

pu_1 = ProductUser()
