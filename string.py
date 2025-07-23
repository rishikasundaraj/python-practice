#Basic String Handling
#Ask the user to enter their name.
# 1.Print the name in uppercase, lowercase, and title case.
name="rishika"
print(name.upper())
print(name.lower())
print(name.title())
#Ask the user to enter a sentence.
# 2.Count how many times the letter "a" appears.
print(name.count("a"))
# 3.Check if a string starts with "Hello" and ends with "!".
string=" Hello! "
print(string.startswith("Hello"))
print(string.endswith("!"))
# 4.Remove all spaces from a string.
print(string.strip())
#Ask the user to enter a word.
# 5.Print the word in reverse using slicing.
print(string[::-1])
#Loops + Strings
# 1.Count how many vowels are in a word using a loop.
word="rishika is a daughter of sundarraj"
vowels="aeiouAEIOU"
count=0
for i in word:
    if i in vowels:
        count+=1
print(count)
#Ask the user for a word.
# 2.Print each letter along with its position (like: 0 → R, 1 → i).
for index in range(len(word)):
    print(index,"_",word[index])
#Ask the user to enter two strings.
# 3.Print which one is longer, or if both are equal in length.
str1="rishika"
str2="chinuumai"
if len(str1)>len(str2):
    print("str1 is greater")
elif len(str1)<len(str2):
    print("str2 is greater")
else:
    print("both are equal")
#Ask the user to enter a sentence.
# 4.Replace all "a" with "@".
print(word.replace("a","@"))
#Check if a string is a palindrome (same forward and backward).
# 5.Example: "madam" → Palindrome, "apple" → Not
text="apple"
if text==text[::-1]:
    print("palindrome")
else:
    print("it is not a palindrome")
