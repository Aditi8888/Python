#name = input("enter your name:")
#print(f"hello{name}")
#name = input("enter your name :")
#age = input("enter your age")
#age = int(age)
#age = age +1
#print(f"hello {name}")
#print(f"you are {age}years old")
age = int(input("enter your age:"))
if  age < 0 :
    print("you have not born yet")
elif  age >= 18 :
    print("you are eligible")
else:
    print("you are not eligible")


name = input("enter your name :")
if name == "" :
    print("you did not type in your name !")
else :
    print(f"hello {name}")