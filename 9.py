'''ЗАДАНИЕ 9:
Напишите SQL-запрос для произведения следующих изменений в базе данных:
 Удалить все данные из таблицы student со сбросом идентификатора в исходное состояние.'''

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

cur.execute("""drop table if exists student""")
conn.commit()

cur.execute("""create table student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar)
""")
conn.commit()

cur.execute("""INSERT INTO student (first_name, last_name, birthday, phone) VALUES
('John', 'Doe', '1990-05-15', '123-456-7890'),
('Alice', 'Smith', '1995-08-21', '987-654-3210'),
('Bob', 'Johnson', '1988-11-30', '555-123-4567')""")
conn.commit()
#Не удаляйте этот код - он нужен для корректной работы тренажера. Пишете свой запрос ниже.
cur.execute("""TRUNCATE TABLE student RESTART IDENTITY""")
conn.commit()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()

