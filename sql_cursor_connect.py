from peewee import *


def conn_sql():
    # suso su postgres
    # psql
    # \l
    # перед началом нужно создать базу данных
    # create database name_db;
    # \connect name_db
    # создать таблицу
    # create table estore( id int NULL, name varchar(100), price int, orders varchar(250));
    #  проверка select * from name_db;

    # Создаем соединение с нашей базой данных
    conn = PostgresqlDatabase(database= 'estore', user='postgres', password='vla', host='localhost')

    # Создаем курсор - специальный объект для запросов и получения данных с базы
    cursor = conn.cursor()


    # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
    cursor.execute("insert into estore values ('111111', 'A Aagrh!', '5646','order somthg') ")

    # Обратите внимание, даже передавая одно значение - его нужно передавать кортежем!
    # Именно по этому тут используется запятая в скобках!
    new_artists = [
        ('A Aagrh!',),
        ('A Aagrh!-2',),
        ('A Aagrh!-3',),]
    cursor.executemany("insert into estore values (Null, %s,'5646','order somthg');", new_artists)

    # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
    conn.commit()

    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    cursor.execute("SELECT * FROM estore")

    # Получаем результат сделанного запроса
    results = cursor.fetchall()
    print(results)

    # Получаем результаты по одному, используя метод курсора .fetchone()
    cursor.execute("SELECT * FROM estore")
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())

    # Использование курсора как итератора
    cursor.execute('SELECT * FROM estore')
    for row in cursor.fetchall():
        print(row)


    # Не забываем закрыть соединение с базой данных
    conn.close()

def main():
    conn_sql()

if __name__ == '__main__':
    main()
