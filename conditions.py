#Ask the user to enter a number.
# 1.Print whether it is positive, negative, or zero.
n=int(input("enter the number"))
if n>0 :
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")
#Ask the user to enter a number.
# 2.Print whether the number is even or odd.
n=int(input("enter the number"))
if n%2==0:
    print("even")
else:
    print("odd")
#Ask the user for their age.
# 3.Print "You can vote" if age is 18 or above, else print "You cannot vote".
n=int(input("enter the age:"))
if n>18:
    print("you are eligible for vote")
elif n<18:
    print("you are not eligible for vote")
else:
    print("invalid")
#Ask the user to enter two numbers.
# 4.Print which number is greater or if they are equal.
n1=int(input("enter the number"))
n2=int(input("enter the number"))
if n1>n2:
    print("the number is greater")
else:
    print("they are equal")

#Ask the user for a number.
# 5.Print "Divisible by both 3 and 5" if it is, otherwise print "Not divisible by both".
n=int(input("enter th number"))
if n%3==0 and n%5==0:
    print("the number is divisible by both 3 and 5")
else:
    print("the number is not divisible by both 3 and 5")
#Ask the user to enter their marks (0 to 100).
# 6.Print the grade:
#(90 and above: Grade A
#75–89: Grade B
#50–74: Grade C
#Below 50: Grade F)
n=int(input("enter the number"))
if n>90:
    print("grade A")
elif n>=90:
    print("grade B")
elif n>75:
    print("grade is C")
#Ask the user to enter a letter.
# 7.Print whether it is a vowel (a, e, i, o, u) or a consonant.
n=input("enter the character")
if n in "aeiou":
    print("vowels")
else:
    print("constant")
#Ask the user to enter a year.
# 8.Print whether it is a leap year or not.
year=int(input("enter the number"))
if ( year%4==0 and year % 100 != 0) or (year % 400 == 0):
    print("it is leap year")
else:
    print("it is not a leap year")
#Ask the user for a number.
# 9.Print whether it is a single-digit number (0–9) or not.
n=int(input("enter the number"))
if n<=9:
    print("single digit")
else:
    print("double digit")
# 10.Display a menu:
#Tea
#Coffee
#Juice
#Ask for the user's choice and print what they selected.
print("1. Tea\n2. Coffee\n3. Juice")
choice = int(input("Choose 1, 2, or 3: "))
if choice == 1:
    print("You chose Tea")
elif choice == 2:
    print("You chose Coffee")
elif choice == 3:
    print("You chose Juice")
else:
    print("Invalid choice")

#If input is invalid, print "Invalid choice".