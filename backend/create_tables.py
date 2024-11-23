#backend/create_tables.py
import psycopg2

conn = psycopg2.connect(#подключение к базе данных
    dbname="server_management_db",#имя базы данных
    user="your_username",#имя пользователя
    password="your_password",#пароль
    host="localhost",#хост (если база на той же машине)
    port="5432"#порт
)

cur = conn.cursor()

#создаем таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS servers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        status VARCHAR(50) NOT NULL,
        cpu INT NOT NULL,
        memory INT NOT NULL,
        disk INT NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        server_id INT REFERENCES servers(id),
        start_time TIMESTAMP NOT NULL,
        end_time TIMESTAMP NOT NULL
    );
""")

conn.commit()

cur.close()#закрываем соединение
conn.close()

print("Tables created successfully!")
