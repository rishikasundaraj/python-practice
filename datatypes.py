#Topic 3: Data Types
# 1.Create variables of type int, float, str, and bool. Print their types.
name="rishika"
age=20
mark=67.5
print(type(name))
print(type(age))
print(type(mark))
# 2.Convert string "123" to an integer and print it.
num=int("123")
print(num)
# 3.Convert number 25 to a string and print its type.
num=str(25)
print(type(num))
# 4.Convert float 5.8 to an integer and print it.
x=int(5.8)
print(x)
# 5.Ask user for a number, convert to float, and multiply by 2.
user=input("enter the number ")
num=float(user)
print(num*2)
# 6.Show the result of: type(10/3) and type(10//3).
print(type(10/3) and type(10/3))
# 7.Try bool("hello"), bool(""), bool(0), and bool(1). Print all.
print(bool("hello"))
print(bool(""))
print(bool(0))
print(bool(1))
# 8.Convert "True" and "False" to real boolean using comparison: == "True".
x = "True"
print(x == "True")
# 9.Ask user input and show its type before and after casting to int.
x = input("Enter a number: ") 
print("Before:",type(x))
x = int(x)
print("After:", type(x)) 
# 10.What is the output of: type(3.0 + 2)?
print(type(3.0+2))
