'''ЗАДАНИЕ 1:

Напишите SQL-запрос для произведения следующих изменений в базе данных: Добавить ограничение на поле unit_price
таблицы products (цена должна быть больше 0).'''


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

cur.execute("""DROP TABLE IF EXISTS products""")

cur.execute("""CREATE TABLE products (
                product_id smallint NOT NULL,
                product_name character varying(40) NOT NULL,
                supplier_id smallint,
                category_id smallint,
                quantity_per_unit character varying(20),
                unit_price real,
                units_in_stock smallint,
                units_on_order smallint,
                reorder_level smallint,
                discontinued integer NOT NULL)
""")
conn.commit()

cur.execute("""INSERT INTO products VALUES
(66, 'Louisiana Hot Spiced Okra', 2, 2, '24 - 8 oz jars', 17, 4, 100, 20, 0),
(67, 'Laughing Lumberjack Lager', 16, 1, '24 - 12 oz bottles', 14, 52, 0, 10, 0),
(68, 'Scottish Longbreads', 8, 3, '10 boxes x 8 pieces', 12.5, 6, 10, 15, 0),
(69, 'Gudbrandsdalsost', 15, 4, '10 kg pkg.', 36, 26, 0, 15, 0),
(70, 'Outback Lager', 7, 1, '24 - 355 ml bottles', 15, 15, 10, 30, 0),
(71, 'Flotemysost', 15, 4, '10 - 500 g pkgs.', 21.5, 26, 0, 0, 0),
(72, 'Mozzarella di Giovanni', 14, 4, '24 - 200 g pkgs.', 34.7999992, 14, 0, 0, 0),
(73, 'Röd Kaviar', 17, 8, '24 - 150 g jars', 15, 101, 0, 5, 0),
(74, 'Longlife Tofu', 4, 7, '5 kg pkg.', 10, 4, 20, 5, 0),
(75, 'Rhönbräu Klosterbier', 12, 1, '24 - 0.5 l bottles', 7.75, 125, 0, 25, 0),
(76, 'Lakkalikööri', 23, 1, '500 ml', 18, 57, 0, 20, 0),
(77, 'Original Frankfurter grüne Soße', 12, 2, '12 boxes', 13, 32, 0, 15, 0)
""")
conn.commit()
#cur.fetchall() #Получить все строки
#cur.fetchone() #Получить одну строку
#cur.fetchmany(5) #Получить N-строк


#Добавляем ограничение
cur.execute("""ALTER TABLE products
ADD CONSTRAINT proverka
CHECK (unit_price > 0)""")
conn.commit()

cur.execute("SELECT * FROM products")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
