from database import *
from tabulate import *


def _input_or_back(prompt):
    value = input(prompt)
    if value.lower() == "b":
        print("Returning to admin menu.")
        return None
    return value


def add_user(role="user"):
    uname = _input_or_back("username (enter b to go back):")
    if uname is None:
        return
    password = _input_or_back("password (enter b to go back):")
    if password is None:
        return
    name = _input_or_back("name (enter b to go back):")
    if name is None:
        return
    email = _input_or_back("email (enter b to go back):")
    if email is None:
        return
    q = "insert into users (username,password,name,email,role) values (%s,%s,%s,%s,%s)"
    cur.execute(q, (uname, password, name, email, role))
    con.commit()
    print('user added successfully')
    
    
def view():
    q="select * from users"
    cur.execute(q)
    data=cur.fetchall()
    head=["ID","USERNAME","PASSWORD","NAME","EMAIL","ROLE"]
    print(tabulate(data,headers=head,tablefmt="solid"))
        
        
def update():
    id = _input_or_back("enter user id (enter b to go back):")
    if id is None:
        return
    id = int(id)
    print("what do you whant to update?")
    print("1.username")
    print("2.password")
    print("3.name")
    print("4.email")
    print("5.role")
    choice = _input_or_back("enter your choice (enter b to go back):")
    if choice is None:
        return
    choice = int(choice)
    if choice==1:
        username = _input_or_back("enter new name (enter b to go back):")
        if username is None:
            return
        q="update users set username='{}' where id={} ".format(username,id)
    elif choice==2:
        password = _input_or_back("enter new password (enter b to go back):")
        if password is None:
            return
        q="update users set password='{}' where id={}".format(password,id)
    elif choice==3:
        name = _input_or_back("enter new name (enter b to go back):")
        if name is None:
            return
        q="update users set name='{}' where id={}".format(name,id)
    elif choice==4:
        email = _input_or_back("enter new email (enter b to go back):")
        if email is None:
            return
        q="update users set email='{}' where id={}".format(email,id)
    elif choice==5:
        role = _input_or_back("enter new role (user/admin, or b to go back):")
        if role is None:
            return
        q="update users set role='{}' where id={}".format(role,id)
    else:
        print("invalid input")
        return
    cur.execute(q)
    con.commit()
    print("update successfull")
    
   
   
def delete():
    id = _input_or_back("enter id to delete (enter b to go back):")
    if id is None:
        return
    q="delete from users where id={}".format(id)
    cur.execute(q)
    con.commit()
    print("deleted successfully")
    