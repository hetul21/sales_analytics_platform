import sqlite3

def create_database():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.executescript("""
                         create table if not exists customers(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name text not null,
                         email text,
                        city text);
                         
                         create table if not exists products(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name text not null,
                         category text,
                         price real not null);

                         create table if not exists orders(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         customer_id integer,
                         order_date text,
                         FOREIGN KEY (customer_id) REFERENCES customers(id));
                         
                         create table if not exists order_items(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         order_id integer,
                         product_id integer,
                         quantity intteger,
                         FOREIGN KEY (order_id) REFERENCES orderS(id),
                         FOREIGN KEY (product_id) REFERENCES products(id)
                         );
                         

                         """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
