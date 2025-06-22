'''ЗАДАНИЕ 4:
Напишите SQL-запрос для произведения следующих изменений в базе данных:
Создать таблицу student с полями
                                student_id (тип serial),
                                first_name (тип varchar),
                                last_name (тип varchar),
                                birthday (тип date),
                                phone (тип varchar).'''


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
#Не удаляйте этот код - он нужен для корректной работы тренажера. Пишете свой запрос ниже.
cur.execute("""CREATE TABLE IF NOT EXISTS student (student_id serial,
                                first_name varchar,
                                last_name varchar,
                                birthday date,
                                phone varchar)""")
conn.commit()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()