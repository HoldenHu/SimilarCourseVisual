# encoding: utf-8

from lib.global_variable import *
import sqlite3


class ModsDB:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        #  This routine creates a cursor that will be used in Python database programming.
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        pass

    ########################################################################################
    #  Function: Store module code & module description to ./db/
    #  Input: int, str, str
    #  Output: Update DB
    ########################################################################################
    def store_to_sqlite(self, id, code, details):
        self.conn = sqlite3.connect(CONSTANT_DB_PATH)

        try:
            self.conn.execute(
                "INSERT INTO Modsinfo (ModsID,ModsCode,ModsDetails) VALUES (?,?,?)",
                (id, code, details))
        except:
            print "insert ERROR"

        self.conn.commit()
        return

    ########################################################################################
    #  Function: Read all data from sqlite3
    #  Input: None
    #  Output: return [(id, code, description),]
    ########################################################################################
    def read_all_from_sqlite(self):
        self.conn.row_factory = sqlite3.Row  # Access to column information
        self.cursor.execute("select * from Modsinfo")  # This routine executes an SQL statement

        # This routine gets all (remaining) rows in the query result set and returns a list.
        # When there are no rows available, an empty list is returned.
        rows = self.cursor.fetchall()
        return rows

    ########################################################################################
    #  Function: Get the descriptions of a module by using ModsCode such as CS5242
    #  Input: str
    #  Output: return "module description"
    ########################################################################################
    def read_details_bycode(self, code):
        self.conn.row_factory = sqlite3.Row  # Access to column information

        # This routine executes an SQL statement
        self.cursor.execute("select ModsDetails from Modsinfo where ModsCode =" + "\"" + code + "\"")

        # This routine gets all (remaining) rows in the query result set and returns a list.
        # When there are no rows available, an empty list is returned.
        rows = self.cursor.fetchall()
        return rows[0][0]

    ########################################################################################
    #  Function: Whether the interpretation of the course exists in the database, Convenient to update the database
    #  Input: str
    #  Output: return True or False
    ########################################################################################
    def if_module_exist(self, code):
        self.conn.row_factory = sqlite3.Row
        self.cursor.execute("select ModsID from Modsinfo WHERE Modscode =" + "\"" + code + "\"")

        row_in_db = self.cursor.fetchall()
        if len(row_in_db) == 0:
            # conn.close()
            return False
        else:
            # conn.close()
            return True

    ########################################################################################
    #  Function: Create a database if the database does not exist
    #  Input: None
    #  Output: Create DB
    ########################################################################################
    # def create_database(self):
        # '''创建游标'''
        # cursor = conn.cursor()

        # '''执行语句'''
        # sql = '''create table Modsinfo (
        #         ModsID int,
        #         ModsCode text,
        #         ModsDetails text)'''

        # cursor.execute(sql)
        # return

