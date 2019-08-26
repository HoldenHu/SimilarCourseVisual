# encoding: utf-8

from lib.global_variable import *
import sqlite3
import logging


class ModsDB:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        #  This routine creates a cursor that will be used in Python database programming.
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        pass

    def store_to_sqlite(self, id, code, details):
        '''
        Store module code & module description to ./db/
        :param id: 1
        :param code: "CS5242"
        :param details: ""word
        :return: Update DB
        '''
        self.conn = sqlite3.connect(CONSTANT_DB_PATH)

        try:
            self.conn.execute(
                "INSERT INTO Modsinfo (ModsID,ModsCode,ModsDetails) VALUES (?,?,?)",
                (id, code, details))
        except Exception,e:
            logging.error('Holden: ERROR:' + str(e))

        logging.info('Holden: Store module - ' + code)
        self.conn.commit()
        return

    def read_all_from_sqlite(self):
        '''
        Read all data from sqlite3
        :return: return [(id, code, description),]
        '''
        self.conn.row_factory = sqlite3.Row  # Access to column information
        self.cursor.execute("select * from Modsinfo")  # This routine executes an SQL statement

        # This routine gets all (remaining) rows in the query result set and returns a list.
        # When there are no rows available, an empty list is returned.
        rows = self.cursor.fetchall()

        logging.info('Holden: Read all from sqlite')
        return rows

    def read_details_bycode(self, code):
        '''
        Get the descriptions of a module by using ModsCode such as CS5242
        :param code: "CS5242"
        :return: "module description"
        '''
        self.conn.row_factory = sqlite3.Row  # Access to column information

        # This routine executes an SQL statement
        self.cursor.execute("select ModsDetails from Modsinfo where ModsCode =" + "\"" + code + "\"")

        # This routine gets all (remaining) rows in the query result set and returns a list.
        # When there are no rows available, an empty list is returned.
        rows = self.cursor.fetchall()
        return rows[0][0]

    def if_module_exist(self, code):
        '''
        Whether the interpretation of the course exists in the database, Convenient to update the database
        :param code: "CS5242"
        :return: return True or False
        '''
        self.conn.row_factory = sqlite3.Row
        self.cursor.execute("select ModsID from Modsinfo WHERE Modscode =" + "\"" + code + "\"")

        row_in_db = self.cursor.fetchall()
        if len(row_in_db) == 0:
            # conn.close()
            return False
        else:
            # conn.close()
            return True

    # def create_database(self):
        # '''
        # Create a database if the database does not exist
        # :return: Create DB
        # '''
        # cursor = conn.cursor()

        # sql = '''create table Modsinfo (
        #         ModsID int,
        #         ModsCode text,
        #         ModsDetails text)'''

        # cursor.execute(sql)
        # return

