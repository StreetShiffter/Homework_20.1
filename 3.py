'''ЗАДАНИЕ 3:

Напишите SQL-запрос для произведения следующих изменений в базе данных: Создать новую таблицу discontinued_products, содержащую все продукты,
снятые с продажи из таблицы skytask.products (discontinued равен 1).'''

import psycopg2
conn = psycopg2.connect(
        dbname="20.1-homework",
        user="postgres",
        password="12345",
        port="5432",
        host="localhost"
)

# Открытие курсора
cur = conn.cursor()

cur.execute("""drop table if exists discontinued_products""")
conn.commit()
#Не удаляйте этот код - он нужен для корректной работы тренажера.
#Пишете свой запрос ниже.

cur.execute("""CREATE TABLE IF NOT EXISTS discontinued_products AS
    SELECT *
    FROM products
    WHERE discontinued = 1""")

conn.commit()

cur.execute("SELECT * FROM discontinued_products")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()