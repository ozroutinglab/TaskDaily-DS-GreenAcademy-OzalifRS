"""
file name: DatabaseDS.py
"""

import os
# from mysql.connector.connection import MySQLConnection
from mysql import connector
from Helper.IniManager import IniManager


class DatabaseDS(object):
    def __init__(self, databasename=str(), host=str()) -> None:
        # print(f"databasename: {databasename}")
        self._configs = IniManager.ReadFile(os.path.abspath("task\\Configurations\\" + "global.ini"))
        self._mysqldb = connector.Connect(
            host=self._configs['DATABASE']['host'],  # default: localhost
            user=self._configs['DATABASE']['user'],
            password=self._configs['DATABASE']['password'],
            database=databasename
        )
        # self.mysqlCursor = self.__mysqldb.cursor()
        # Return DB Connection Object
    #
    def GetDatabaseConnection(self):
        return self._mysqldb

    def Create(self, tableName, dataTobeInserted=dict()):
        cursor = self._mysqldb.cursor()

        columnSection = ""
        dataSection = ""
        insertQuery = "INSERT INTO %s (%s) VALUES (%s)"
        listColumn = list()
        listData = list()

        for key, value in dataTobeInserted.items():
            listColumn.append(key)
            listData.append("'" + value + "'")
        # result: column1, column2, ..., column-n
        columnSection = ",".join(listColumn)
        dataSection = ",".join(listData)
        insertQuery = insertQuery % (tableName, columnSection, dataSection)
        print("Query insert: " + insertQuery)

        try:
            cursor.execute(insertQuery)
            self._mysqldb.commit()
        except connector.Error as err:
            self._mysqldb.rollback()
            try:
                print(f"MySQL Error [{err.args[0]}]: {err.args[1]}")
                return False, f"Failed, [{err.args[0]}]: {err.args[1]}"
            except IndexError:
                print(f"MySQL Error: {err}")
                return False, f"Failed, {err}"
        except TypeError as err:
            self._mysqldb.rollback()
            print(err)
            return False, f"Failed, {err}"
        except ValueError as err:
            self._mysqldb.rollback()
            print(err)
            return False, f"Failed, {err}"
        finally:
            print(">> Finally, cursor is closed")
            cursor.close()
        #
        return True, "Success"

    #

    # DONE
    def Read(self, column=list(), table=str(), whereClause=dict(), isDictionary=True):
        # cursor = self._mysqldb.cursor(dictionary=True)
        cursor = self._mysqldb.cursor(dictionary=isDictionary)
        results = None
        sql, subsqlWhere = self.GetSQLSelect()
        colStr = str()
        whereStr = str()
        whereList = list()

        if len(column) == 0:
            colStr = "*"
        else:
            colStr = ", ".join(column)

        if whereClause:
            for key, value in whereClause.items():
                whereList.append(f"{key} = '{value}'")
            whereStr = " and ".join(whereList)
            sql += subsqlWhere
            sql = sql % (colStr, table, whereStr)
        else:
            sql = sql % (colStr, table)
        #
        # print(f">> colStr:\n{colStr}")
        # print(f">> whereStr:\n{whereStr}")
        # print(f">> SQL:\n{sql}")
        try:
            # cursor.execute(sql, [(colStr), (table), (whereStr)])
            cursor.execute(sql)
            results = cursor.fetchall()
        except connector.Error as err:
            self._mysqldb.rollback()
            try:
                print(f"MySQL Error [{err.args[0]}]: {err.args[1]}")
                return False, None, f"Failed, [{err.args[0]}]: {err.args[1]}"
            except IndexError:
                print(f"MySQL Error: {err}")
                return False, None, f"Failed, {err}"
        except TypeError as err:
            self._mysqldb.rollback()
            print(err)
            return False, None, f"Failed, {err}"
        except ValueError as err:
            self._mysqldb.rollback()
            print(err)
            return False, None, f"Failed, {err}"
        finally:
            print(">> Finally, cursor is closed")
            cursor.close()
        #
        if len(results) < 1:
            return False, results, "No data"
        return True, results, "Success"

    def GetSQLSelect(self):
        sql = "SELECT %s FROM %s"
        subsqlWhere = " WHERE %s"
        return sql, subsqlWhere

    #

    def Update(self, tableName, dataTobeUpdated=dict(), dataWhere=dict()):
        cursor = self._mysqldb.cursor()

        updateQuery = "UPDATE %s SET %s WHERE %s"
        colDataSection = ""
        whereSection = ""
        listColData = list()
        listWhere = list()

        # Full config SET
        for column, value in dataTobeUpdated.items():
            listColData.append(column + " = '" + value + "'")
        colDataSection = ",".join(listColData)

        # Full config WHERE
        if len(dataWhere) > 0:
            for column, value in dataWhere.items():
                listWhere.append(f"{column} = {value}")
            whereSection = " and ".join(listWhere)
            updateQuery = updateQuery % (tableName, colDataSection, whereSection)
        #
        print("Query update: " + updateQuery)

        try:
            cursor.execute(updateQuery)
            self._mysqldb.commit()
        except connector.Error as err:
            self._mysqldb.rollback()
            try:
                print(f"MySQL Error [{err.args[0]}]: {err.args[1]}")
                return False, f"Failed, [{err.args[0]}]: {err.args[1]}"
            except IndexError:
                print(f"MySQL Error: {err}")
                return False, f"Failed, {err}"
        except TypeError as err:
            self._mysqldb.rollback()
            print(err)
            return False, f"Failed, {err}"
        except ValueError as err:
            self._mysqldb.rollback()
            print(err)
            return False, f"Failed, {err}"
        finally:
            print(">> Finally, cursor is closed")
            cursor.close()
        #
        return True, "Success"

    #

    def Delete(self, table=str(), whereClause=dict()):
        cursor = self._mysqldb.cursor()

        updateQuery = "DELETE FROM %s WHERE %s"
        whereSection = ""
        listWhere = list()

        # Full config WHERE
        if len(whereClause) > 0:
            for column, value in whereClause.items():
                listWhere.append(f"{column} = {value}")
            whereSection = " and ".join(listWhere)
            updateQuery = updateQuery % (table, whereSection)
        #
        print("Query update: " + updateQuery)

        try:
            cursor.execute(updateQuery)
            self._mysqldb.commit()
        except connector.Error as err:
            self._mysqldb.rollback()
            try:
                print(f"MySQL Error [{err.args[0]}]: {err.args[1]}")
                return False, f"Failed, [{err.args[0]}]: {err.args[1]}"
            except IndexError:
                print(f"MySQL Error: {err}")
                return False, f"Failed, {err}"
        except TypeError as err:
            self._mysqldb.rollback()
            print(err)
            return False, f"Failed, {err}"
        except ValueError as err:
            self._mysqldb.rollback()
            print(err)
            return False, f"Failed, {err}"
        finally:
            print(">> Finally, cursor is closed")
            cursor.close()
        #
        return True, "Success"

    #

    def __del__(self):
        self._mysqldb.close()
        del self._mysqldb
        print("DB Destroy")

    # endDel
