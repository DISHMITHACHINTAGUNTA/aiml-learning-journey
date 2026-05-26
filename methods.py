# peru=input("mee peru chepandi :")
# k=peru.find("dis")
# print(k)

text = input("Type your paragraph: ")
word = input("Enter the word or letter to search for: ")
n = int(input("Which occurrence do you want? "))

start = -1
for i in range(n):
    start = text.rfind(word, start + 1,800)
    print(start)
    if start ==-1:
        break