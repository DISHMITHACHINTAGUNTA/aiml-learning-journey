peru=input("enter your peru:")
rs=peru.find(" ")
print("your peru doesn't contain kallilu raa" if rs == -1 else peru[rs] )

# if ,elif stmts

if len(peru)>= 12:
    print("your name can't be more than 12 characters")
elif not peru.find(" ") == -1:
    print("your name can't contain spaces")
elif not peru.isalpha():
    print("your name can't contain numbers")
else:
    print("heyy manava or manavi ",peru)