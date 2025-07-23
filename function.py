#Basic Function Definitions
# 1.Write a function greet() that prints "Hello, Rishika!".
def greet():
    print("hello world!")
greet()
# 2.Write a function add(a, b) that takes two numbers and returns their sum.
def add(a,b):
    return a+b
result=add(4,5)
print(result)
# 3.Write a function is_even(n) that returns True if the number is even, otherwise False.
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
result=is_even(5)
print(result)

#or
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# 4.Write a function print_table(n) that prints the multiplication table of n from 1 to 10.
def print_table(n):
    for i in range(1,10):
        print(f"{n}x{i}={n*i}")
print_table(8)
# 5.Write a function square_list(numbers) that takes a list and returns a list of squares.
def square_list(numbers):
    squares=[]
    for num in numbers:
        squares.append(num**2)
    return squares
nums=[1,2,3,4,5]
print(square_list(nums))
 
 
#Functions with Conditions and Loops
# 1.Write a function count_vowels(word) that returns the number of vowels in the word.
def count_vowels(word):
    vowels="aeiou"
    count=0
    for char in word:
        if char in vowels:
            count+=1
    return count
print(count_vowels("rishika"))

# 2.Write a function is_palindrome(word) that returns True if the word is a palindrome.
def is_palindrome(word):
    word = word.lower()  # Convert to lowercase for case-insensitive comparison
    return word == word[::-1]
print(is_palindrome("madam"))
# 3.Write a function factorial(n) that returns the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 4.Write a function max_of_list(lst) that finds the maximum number in a list without using max().
def max_of_list(lst):
    max_num=lst[0]
    for num in lst:
        if num > max_num:
            max_num=num
    return max_num
print(max_of_list([1,2,3,56,78,45]))
#Write a function login(username, password) that prints "Login successful" if the username is "admin" and password is "1234", else prints "Invalid login".
def login(username,password):
    if username=="admin" and password=="12345":
         print("login successfully")
    else:
        print("invalid")
login("admin","12345")
