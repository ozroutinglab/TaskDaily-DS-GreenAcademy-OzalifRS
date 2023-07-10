'''
File name : Sesi05_task_01.py
Desc      : Lanjutkan kode terlampir untuk insert SQL nya.
            Kalau ada yang bisa buat pilihan (edit/insert/delete) nya
            bisa LEBIH BAIK
'''

from Engine.Sesi05SchoolApp import SchoolApp


if __name__ == "__main__":
    # pass
    schoolApp = SchoolApp()
    isLoginSuccessful = False

    while not isLoginSuccessful:
        result = schoolApp.Login()
        # print(f"MAIN >> result 0: {result[0]}")
        # print(f"MAIN >> result 1: {result[1]}")
        if result[0]:
            isLoginSuccessful = True
            schoolApp.MainApp()
        else:
            # When username and/or password incorrect
            isRedoLogin = schoolApp.LoginFail()
            # print(f"MAIN >> isRedoLogin: {isRedoLogin}")

            if not isRedoLogin:
                break
            else:
                continue
            #
        #
    #
# endMain
