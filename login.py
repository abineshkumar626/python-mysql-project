from database import *


def login():
    username=input("enter your username:")
    password=input("enter your password:")
    q="select * from users where username='{}' and password='{}'".format(username,password)
    cur.execute(q)
    data=cur.fetchone()
    return data   
