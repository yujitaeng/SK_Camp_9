# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "squirrel",
    password = "squirrel",
    database = "menudb"
)

cursor = connection.cursor()
sql = "INSERT INTO tbl_menu(menu_name, menu_price, category_code, orderable_status) VALUES(%s, %s, %s, %s)"
values = ('쌀국수', 10000, 4, 'Y')

cursor.execute(sql, values)
connection.commit()

print(f'{cursor.rowcount}개의 행을 삽입하였습니다')

cursor.close()
connection.close()
