import sqlite3

with sqlite3.connect("mySQL.sqlite3") as db:
    cursor = db.cursor()

    query = """ SELECT * FROM Vegetables_and_Fruits """
    cursor.execute(query)
    for res in cursor:
        print(res)

    query2 = """ SELECT * FROM Vegetables_and_Fruits WHERE type = 'овощ' """
    cursor.execute(query2)
    print('Отображение всех овощей')
    for res in cursor:
        print(res)

    query3 = """ SELECT * FROM Vegetables_and_Fruits WHERE type = 'фрукт' """
    cursor.execute(query3)
    print('Отображение всех фруктов')
    for res in cursor:
        print(res)
# result = cursor.fetchall()
#
# for row in result:
#     print(row)

# conn.close()
