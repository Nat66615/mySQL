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

    query4 = """ SELECT name FROM Vegetables_and_Fruits """
    cursor.execute(query4)
    print('Отображение всех названий овощей и фруктов')
    for res in cursor:
        print(res)

    query5 = """ SELECT DISTINCT color FROM Vegetables_and_Fruits """
    cursor.execute(query5)
    print('Отображение всех цветов(уникальные)')
    for res in cursor:
        print(res)

    query6 = """ SELECT name FROM Vegetables_and_Fruits WHERE type = 'фрукт' AND color = 'зеленый' """
    cursor.execute(query6)
    print('Отображение фруктов конкретного цвета')
    for res in cursor:
        print(res)

    query7 = """ SELECT name FROM Vegetables_and_Fruits WHERE type = 'овощ' AND color = 'желтый' """
    cursor.execute(query7)
    print('Отображение овощей конкретного цвета')
    for res in cursor:
        print(res)
