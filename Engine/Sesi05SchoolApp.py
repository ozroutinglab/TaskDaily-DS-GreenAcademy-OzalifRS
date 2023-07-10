'''
File name: Sesi05SchoolApp.py
'''

import os
from Helper.DatabaseDS import DatabaseDS
from Helper.IniManager import IniManager


class SchoolApp(object):
    def __init__(self, datasourceOption='sesi5schoolpython.ini') -> None:
        # pass
        self._configs = IniManager.ReadFile(os.path.abspath("task\\Configurations\\" + datasourceOption))
        self.__db = DatabaseDS(databasename=self._configs['DB_SOURCE']['dbname'])
    #

    def Login(self):
        un = input('Type your username: ')
        pwd = input('Type your password: ')
        # print(f"username: {un}, and password: {pwd}")

        results = self.__db.Read(table="users", whereClause={
            'username': un,
            'userpassword': pwd
        })

        # import mysql.connector
        # mysqldb=mysql.connector.Connect(host="adminlab-VBOX",user="root",password="12345",database="school")
        # mycursor=mysqldb.cursor()

        # un=input('Type your username: ')
        # pwd=input('Type your password: ')
        # sql="select * from users where username= %s and userpassword=%s"
        # mycursor.execute(sql,[(un),(pwd)])
        # results=mycursor.fetchall()

        # print(results[0])
        # print(results[1])
        # print(results[2])
        return results[0], results[2]
    #

    def LoginFail(self) -> str:
        print("**************************************************")
        print("* Entering incorrect Username and/or password    *")
        optionRelogin = input("Would you like to try again? (Y/n) ")

        return optionRelogin.lower() == "y" or optionRelogin.lower() == "yes"
    #

    def MainApp(self):
        option = int()
        while True:
            os.system('cmd /c cls')
            print()
            print("**************************************************")
            print("***         WELCOME to USER MANAGEMENT         ***")
            print("**************************************************")
            print("*                                                *")
            print("* Please, select your option                     *")
            print("* 1. List all user(s)                            *")
            print("* 2. Insert new user data                        *")
            print("* 3. Update current data                         *")
            print("* 4. Delete any selected data                    *")
            print("* 5. Exit                                        *")
            print("*                                                *")
            print("**************************************************")
            option = int(input("Type your option (1/2/3/4/5): ... "))

            if option == 1:
                print("**************************************************")
                print("* Entering List users data                       *")
                self.ListAllusersDataView()
                continue
            elif option == 2:
                print("**************************************************")
                print("* Entering Insert New User data                  *")
                self.InsertNewUser()
                continue
            elif option == 3:
                print("**************************************************")
                print("* Entering Update User's data                    *")
                self.UpdateUserData()
                continue
            elif option == 4:
                print("**************************************************")
                print("* Entering Delete User's data                    *")
                self.DeleteUserData()
                continue
            elif option == 5:
                print("**************************************************")
                print("* EXITING.............                           *")
                break
            else:
                print("**************************************************")
                print("* Please enter the correct option:               *")
                continue
            #
        #
    #

    def ListAllusersDataView(self):
        # pass
        # print("**************************************************")
        # print("*                                                *")

        results = self.ListAllusersData()
        self.ViewResults(results)
        option = "n"

        while option != "y":
            option = input(" Back to the Main Menu? (Y/n) .. ").lower()
        #
    #

    def ListAllusersData(self):
        return self.__db.Read(table="users")
    #

    def InsertNewUser(self):
        # pass
        print("**************************************************")
        print("*                                                *")

        option = "n"
        newUsername = input(" Type new username: ")
        newPassword = input(" Type your new password: ")
        confirmNewPassword = input(" Confirm your new password: ")

        if newPassword == confirmNewPassword:
            # pass
            results = self.__db.Create(
                tableName='users',
                dataTobeInserted={
                    'username': newUsername,
                    'userpassword': newPassword
                }
            )
            print(f" Status: {results[1]}")
        else:
            print(" Password and confirm password do not matched. Try again")
            self.InsertNewUser()

        while option != "y":
            option = input(" Back to the Main Menu? (Y/n) .. ").lower()
        #
    #

    def UpdateUserData(self):
        # pass
        print("**************************************************")
        print("*                                                *")

        option = "n"
        results = self.ListAllusersData()
        self.ViewResults(results)

        print()
        userid = int(input(" Enter user ID data to be updated: "))
        newUsername = input(" Edit new username: ")
        newPassword = input(" Edit your new password: ")
        confirmNewPassword = input(" Confirm your new password: ")

        if newPassword == confirmNewPassword:
            # pass
            results = self.__db.Update(
                tableName='users',
                dataTobeUpdated={
                    'username': newUsername,
                    'userpassword': newPassword
                },
                dataWhere={
                    'personID': userid
                }
            )
            print(f" Status: {results[1]}")
        else:
            print(" Password and confirm password do not matched. Try again")
            self.UpdateUserData()

        while option != "y":
            option = input(" Back to the Main Menu? (Y/n) .. ").lower()
        #
    #

    def DeleteUserData(self):
        # pass
        print("**************************************************")
        print("*                                                *")
        
        results = self.ListAllusersData()
        self.ViewResults(results)
        option = "n"
        
        useridOption = int(input(" Type in the User ID wish to be deleted: .. "))
        results = self.__db.Delete(
            table='users',
            whereClause={
                'personID': useridOption
            }
        )
        # print(f" Status: {results[1]}")

        while option != "y":
            option = input(" Back to the Main Menu? (Y/n) .. ").lower()
        #
    #

    def ViewResults(self, results):
        # print(f">> type:\n{type(results)}")
        # print(f">> results:\n{results}")

        if results[1]:
            strTitleView = "| "
            for keyTitle in results[1][0].keys():
                strTitleView += f"{keyTitle} | "
            #
            print(strTitleView)
            for currentRow in results[1]:
                strResultsView = "| "
                for columnKey in currentRow:
                    strResultsView += f"{currentRow[columnKey]} | "
                #
                print(strResultsView)
            print("--------------------------------")
            #
        #
    #

    def __del__(self):
        # pass
        del self.__db
    #
#
