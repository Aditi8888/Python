name = input("enter your name :")
total = 500
mark1 = float(input("enter your marks for subject1 :"))
mark2 = float(input("enter your marks for subject2 :"))
mark3 = float(input("enter your marks for subject3 :"))
mark4 = float(input("enter your marks for subject4 :"))
mark5 = float(input("enter your marks for subject5 :"))
total_marks = int(mark1 + mark2 +mark3 + mark4+ mark5)
result = (total_marks/total)*100
print(f"{result} %")
if result >=98 :
    print("Grade : A")
elif result >=80 :
    print("Grade :B")
elif result >= 70 :
    print("Grade : C")
elif result >= 60 :
    print("Grade : D")
elif result >= 50 :
    print("Grade: E")
else :
    print("Below average!")
