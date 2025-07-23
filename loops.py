# 1.Print numbers from 1 to 10 using a loop.
for i in range(1,11):
   print(i)
# 2.Print the even numbers from 1 to 20.
for i in range(2,21,2):
   print(i)
# 3.Print the sum of numbers from 1 to 100.
total=0
for i in range(1,101):
   total+=i
print(total)
# 4.Ask the user for a number n and print the multiplication table of n (from 1 to 10).
n=int(input("enter the number:"))
for i in range(1,11):
   print(n,"x",i,"=",n*i)
# 5.Print all numbers from 1 to 50 that are divisible by 5.
for i in range(1,51):
   if i%5==0:
      print(i)
# 6.Ask the user to enter 5 numbers and print the total sum.
total=0
for i in range(5):
   n=int(input("enter the numbers"))
   total+=n
print(total)
# 7.Print the factorial of a number n.9
#(Factorial of 5 is 5×4×3×2×1 = 120)
n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
   fact*=i
print(fact)
# `8.Print all the letters in your name, one by one.
str="rishika"
for char in str:
   print(char)
# 9.Ask the user for a word and count how many vowels are in it.
word=input("enter the char:")
vowel_count=0
for char in word.lower():
   if char in "aeiou":
      vowel_count+=1
print(vowel_count)
# 10.Keep asking the user to enter a number until they type 0, then print the total sum.
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total Sum:", total)
# 11.Print numbers 1 to 5(using loop)
i=1
while i<=5:
   print(i)
   i+=1
# 12.Sum of numbers from 1 to 10
i=1
sum=0
while i<=10:
   sum+=i
   i+=1
print(sum)
# 13.Take input until user enters "exit"
while True:
   text=input("enter the char")
   if text=="exit":
    break
print("you said",text)
# 14Infinite loop (don’t run this forever!)
while True:
    print("I will never stop...")
    

