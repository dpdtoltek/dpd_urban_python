import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')

    for i in range(1, 5):
        check_title = cursor.execute('SELECT * FROM Products WHERE title=?', (f'Продукт {i}',))
        if check_title.fetchone() is None:
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                           (f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products
