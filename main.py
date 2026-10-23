from login import login
from admin import *
from user import *
from database import *

while True:
    print('---LOGIN---')
    print('1.admin login')
    print('2.user login')
    print('3.exit')
    choice=int(input('enter your choice:'))
    if choice==1:
        user=login()
        if user and user[5]=="admin":
            while True:
                print("--admin menu--")
                print("1.add user")
                print("2.add admin")
                print("3.view user")
                print("4.update user")
                print("5.delete user")
                print("6.logout")
                
                ch=int(input('enter your choice:'))
                
                if ch==1:
                    add_user()
                elif ch==2:
                    add_user("admin")
                elif ch==3:
                    view()
                elif ch==4:
                    update()
                elif ch==5:
                    delete()
                elif ch==6:
                    break
                else:
                    print('invalid choice')
        else:
            print('invalid admin login')
         
    elif choice==2:
        user=login()
        if user and user[5]=="user":    
            while True:
                print('--user menu--')
                print('1.view')
                print('2.update name and email')
                print('3.change password')
                print('4.logout')
                ch=int(input('enter your choice:'))
                if ch == 1:
                    view_profile(user[1])
                elif ch==2:
                    update_name_and_password(user[0])
                elif ch==3:
                    update_password(user[0])
                elif ch ==4:
                    break
                else:
                    print('invalid choice')
        else:
            print('invalid user login')
    elif choice==3:
        print('thank you')
        break
     
    else:
        print('invalid choice')