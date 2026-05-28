# Input Validation & While Loop Practice

user_name=input("enter your name:")
attempts=0
while user_name=="":
     print("you didn't entered your name...Oops!")
     user_name=input("please enter your name:")
     attempts+=1
     if user_name != "":
        print("you have successfully entered your name")
if attempts>=3 :
    print("sorry to say this,you took too many trails to enter your name." )
else :

    print(f" hii there {nm}.how is life going?")
