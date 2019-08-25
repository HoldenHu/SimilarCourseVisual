#_*_ coding: utf-8_*_

"""
Store module code & module description to ./db/db.sqlite3
'''create table Modsinfo (
         ModsID int,
         ModsCode text,
         ModsDetails text)'''
"""

import sqlite3
import lib.global_variable

CONSTANT_DB_PATH = "../db/db.sqlite3"

def create_database():
    # '''创建游标'''
    # cursor = conn.cursor()

    # '''执行语句'''
    # sql = '''create table Modsinfo (
    #         ModsID int,
    #         ModsCode text,
    #         ModsDetails text)'''

    # cursor.execute(sql)
    return


#  Store module code & module description to ./db/
#  id (int), code (str), details (str)
def store_to_sqlite(id, code, details):
    conn = sqlite3.connect(CONSTANT_DB_PATH)

    try:
        conn.execute(
            "INSERT INTO Modsinfo (ModsID,ModsCode,ModsDetails) VALUES (?,?,?)",
                     (id, code, details))
    except:
        print "insert ERROR"

    conn.commit()
    conn.close()
    return


#  Read data from sqlite3
#  db_path (str), //exect_cmd (str)
def read_all_from_sqlite(db_path):
    conn = sqlite3.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor = conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory = sqlite3.Row     # 可访问列信息
    cursor.execute("select * from Modsinfo")    #该例程执行一个 SQL 语句

    rows = cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    conn.close()
    return rows


#  Read data from sqlite3
#  db_path (str), //exect_cmd (str)
def read_details_bycode(db_path, code):
    conn = sqlite3.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor = conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory = sqlite3.Row     # 可访问列信息
    cursor.execute("select ModsDetails from Modsinfo where ModsCode =" + "\"" + code + "\"")    #该例程执行一个 SQL 语句

    rows = cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    conn.close()
    return rows[0][0]


#  code (str)
def if_module_exist(code):
    conn = sqlite3.connect(CONSTANT_DB_PATH)
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    cursor.execute("select ModsID from Modsinfo WHERE Modscode =" + "\"" + code + "\"")

    row_in_db = cursor.fetchall()
    if len(row_in_db) == 0:
        conn.close()
        return False
    else:
        conn.close()
        return True

# if __name__=="__main__":
#     print read_details_bycode(CONSTANT_DB_PATH, "CS5242")



