import sqlite3
conn = sqlite3.connect('users')
cursor = conn.cursor()
cursor.execute("""create table if not exists users( id integer primary key, name text, email text)""")
conn.commit()


def insert(id, name, email):
    cursor = conn.cursor()
    cursor.execute("""insert into users  (id, name, email) values (:id,:name,:email) """,
                   {"id": id, "name": name, "email": email})
    conn.commit()


def select():
    cursor = conn.cursor()
    cursor.execute("""select * from users""")
    print(cursor.fetchall())


def select_user(id):
    cursor = conn.cursor()
    cursor.execute("""select * from users where id=:id""", {"id": id})
    print(cursor.fetchall())


def delete_user(id):
    cursor = conn.cursor()
    cursor.execute("""delete from users where id=:id""", {"id": id})
    print(cursor.fetchall())
    conn.commit()


def main():
    insert(1, 'Виктор', 'victor@mail.ru')
    insert(2, 'Олег', 'oleg@mail.ru')


    select()
    select_user(1)
    delete_user(2)
    select()

main()
conn.close()
