from database import *
from tabulate import *


def add_user():
    uname=input("username:")
    password=input("password:")
    name=input("name :")
    email=input("email:")
    q="insert into users (username,password,name,email,role)values('{}','{}','{}','{}','user');".format(uname,password,name,email)
    cur.execute(q)
    con.commit()
    print('user added successfully')
    
    
def view():
    q="select * from users"
    cur.execute(q)
    data=cur.fetchall()
    head=["ID","USERNAME","PASSWORD","NAME","EMAIL","ROLE"]
    print(tabulate(data,headers=head,tablefmt="solid"))
        
        
def update():
    id=int(input("enter user id :"))
    print("what do you whant to update?")
    print("1.username")
    print("2.password")
    print("3.name")
    print("4.email")
    print("5.role")
    choice=int(input("enter your choice:"))
    if choice==1:
        username=input("enter new name:")
        q="update users set username='{}' where id={} ".format(username,id)
    elif choice==2:
        password=input("enter new password")
        q="update users set password='{}' where id={}".format(password,id)
    elif choice==3:
        name=input("enter new name:")
        q="update users set name='{}' where id={}".format(name,id)
    elif choice==4:
        email=input("enter new email:")
        q="update users set email='{}' where id={}".format(email,id)
    elif choice==5:
        role=input("enter new role (user/admin):")
        q="update users set role='{}' where id={}".format(role,id)
    else:
        print("invalid input")
        return
    cur.execute(q)
    con.commit()
    print("update successfull")
    
   
   
def delete():
    id=input("enter id to delete:")
    q="delete from users where id={}".format(id)
    cur.execute(q)
    con.commit()
    print("deleted successfully")
    