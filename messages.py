from db import db
import users
from sqlalchemy.sql import text

def send(header, content):
    user_id = users.user_id()
    votes=0
    sql = text("INSERT INTO messages (header, content, sent, user_id, votes) VALUES (:header, :content, NOW(), :user_id, :votes)")
    db.session.execute(sql, {"header":header, "content":content, "user_id": user_id, "votes": votes})
    db.session.commit()
    return True

def get_messages():
    sql = text("""
               SELECT M.header, M.content, U.username, M.sent 
               FROM messages M, users U 
                WHERE M.user_id=U.id 
               ORDER BY M.sent DESC
               """)
    result = db.session.execute(sql)
    return result.fetchall()

def my_messages():
    user_id=users.user_id()
    sql = text("""
               SELECT M.header, M.content, U.username, M.sent 
               FROM messages M, users U 
                WHERE M.user_id= :user_id and U.id= :user_id
               ORDER BY M.id
               """)
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()