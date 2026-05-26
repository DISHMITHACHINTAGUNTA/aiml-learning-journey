s=input("enter a string of parathesis:")
st = []
r = '([{'
for p in s:
    if p in r:
        st.append(p)
    elif st and ((st[-1] == "(" and p == ")") or (st[-1] == "[" and p == "]") or (st[-1] == "{" and p == "}")):
        st.pop()
    else:
        st.append(p)
if st:
    print("False")
else:
    print("True")
