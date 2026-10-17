from database import *

def view_profile(username):
    q="select * from users where username='{}'".format(username)
    cur.execute(q)
    data=cur.fetchone()
    print("your details ")
    print("id:",data[0])
    print("username:",data[1])
    print("name:",data[3])
    print("mail:",data[4])
    
    
def update_name_and_password(id):
    cid=int(input('enter your id :'))
    if cid == id :
        uname=input('enter new username:')
        pwd=input('enter new password:')
        q="update users set username='{}',password='{}' where id={} ".format(uname,pwd,cid)
        cur.execute(q)
        con.commit()
        print('update successfull')
    else:
        print('invalid id. pls enter valid id!!')   
        
def update_password(id):
    cid=int(input('enter your id:'))
    if cid == id :
        pwd=input('enter new password:')
        q="update users set password='{}' where id='{}'".format(pwd,cid)
        cur.execute(q)
        con.commit()
        print("update successfull")