import pymysql
from config import db
import json

class database:
    def getCursor():
        con = pymysql.connector.connect(
            host=db["host"],
            user=db["user"],
            passwd=db["pwd"],
            database=db["database"]
        )
        cur = con.cursor(prepared=True)
        cur.execute("SET NAMES 'utf8mb4'")
        cur.execute("SET CHARACTER SET 'utf8mb4'")
        return con, cur

# 用于检测是否收集了信息
    def getInfo(open_id):
        (con, cur) = database.getCursor()
        cur.execute("SELECT uid, nickname, phone, email FROM users WHERE open_id=?", [open_id])
        r = cur.fetchone()
        cur.close()
        con.close()
        if r is None:
            return None
        else:
            return [r[0], str(r[1], 'utf-8'), str(r[2], 'utf-8'), str(r[3], 'utf-8')]

#通过用户的id获取相关信息，胶囊的发送者与接收者
    def getInfoByUID(uid):
        (con, cur) = database.getCursor()
        cur.execute("SELECT uid, nickname, phone, email FROM users WHERE uid=?", [uid])
        r = cur.fetchone()
        cur.close()
        con.close()
        if r is None:
            return None
        else:
            return [r[0], str(r[1], 'utf-8'), str(r[2], 'utf-8'), str(r[3], 'utf-8')]

#收集用户信息
    def insertInfo(open_id, nickname, phone, email):
        (con, cur) = database.getCursor()
        cur.execute("INSERT INTO users(open_id, nickname, phone, email) VALUES (?, ?, ?)",[open_id, nickname, phone, email])
        cur.close()
        con.commit()
        con.close()

#塞入给Ta的胶囊
    def insertToTaCapsule(sender_name, receiver_name, receiver_tel, receiver_email, time_limit, cap_template, cap_location, content_word, content_pic, content_voice, registered, sent, content_name, content_phone, content_birth):
        (con, cur) = database.getCursor()
        cur.execute("INSERT INTO toTaCapsules( code, sender_name, receiver_name, receiver_tel, receiver_email, time_limit, cap_template, cap_location, content_word, content_pic, content_voice, registered, sent, content_name, content_phone, content_birth) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",[None, sender_name, receiver_name, receiver_tel, receiver_email, time_limit, cap_template, cap_location, content_word, content_pic, content_voice, registered, sent, content_name, content_phone, content_birth])
        cur.close()
        con.commit()
        con.close()

#塞入给自己的胶囊
    def insertSelfCapsule(open_id, time_limit, cap_template, cap_location, content_word, content_pic, content_voice, registered, sent):
        (con, cur) = database.getCursor()
        info = database.getInfo(open_id)
        cur.execute("INSERT INTO selfCapsules(sender_id, time_limit, cap_template, cap_location, content_word, content_pic, content_voice, registered, sent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",[info[0], time_limit, cap_template, cap_location, content_word, content_pic, content_voice, registered, sent])
        cur.close()
        con.commit()
        con.close()

#塞入给陌生人的胶囊
    def insertStraengerCpasule(open_id, time_limit, cap_template, cap_location, content_word, content_pic, content_voice):
        (con, cur) = database.getCursor()
        info = database.getInfo(open_id)
        cur.execute("INSERT INTO strangerCapsules(sender_id, time_limit, cap_template, cap_location, content_word, content_pic, content_voice) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",[info[0], time_limit, cap_template, cap_location, content_word, content_pic, content_voice])
        cur.close()
        con.commit()
        con.close()



