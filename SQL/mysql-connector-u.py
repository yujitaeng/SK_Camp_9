# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "squirrel",
    password = "squirrel",
    database = "menudb"
)

sql = 'UPDATE tbl_menu SET menu_name = %s, menu_price = %s WHERE menu_code = 1'
values = ('쌀국수', 8500)

cursor = connection.cursor()
cursor.execute(sql, values)
connection.commit()

print(f'{cursor.rowcount}개의 행이 업데이트 되었습니다.')

cursor.close()
connection.close()
