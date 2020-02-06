import sqlite3
import os
def createTable():
    try:
        sql = 'create table if not exists ' \
              'park_info(id varchar(50), pw varchar(20), visitor varchar(20), building varchar(20), phone_num varchar(20), company varchar(20), ' \
               'vehicle varchar(20), reason varchar(20))'
        db = sqlite3.connect('lge_park_info.db')
        db.execute( sql )
        db.close()
        print("DB 생성성공")
    except Exception as err:
        print("DB 생성실패", err)
def insertTable(id, pw, visitor, building, phone_num, company, vehicle, reason):
    try:
        sql = "insert into park_info values(?,?,?,?,?,?,?,?)"
        db = sqlite3.connect('lge_park_info.db')
        db.execute( sql,(id, pw, visitor, building, phone_num, company, vehicle, reason) )
        db.commit()
        db.close()
        print("DB 추가성공")
    except Exception as err:
        print("DB 추가실패", err)
def inputData(my_id, my_pw, visitor, building, phone_num, company, vehicle_num, reason):
    try :
        sql = "delete from park_info "
        db = sqlite3.connect('lge_park_info.db')
        db.execute(sql)
        db.commit()
        db.close()
        print("DB 삭제성공")
    except Exception as err:
        print("DB 삭제실패", err)

    insertTable(my_id, my_pw, visitor, building, phone_num, company, vehicle_num, reason)

def selectTable():
    if os.path.isfile('lge_park_info.db'):
        try:
            sql = "select * from park_info"
            db = sqlite3.connect('lge_park_info.db')
            cur = db.cursor()
            cur.execute( sql )
            data = cur.fetchall()
            db.close()
            return data
        except Exception as err:
            print("에러", err)
            return None
    else :
        return None
