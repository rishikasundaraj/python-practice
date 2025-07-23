#Basic List Operations
# 1.Create a list of 5 fruits.
#Print the first and last fruit.
list=["apple","orange","banana","mango","guva"]
print("first fruit:",list[0])
print("last fruit:",list[4])
# 2.Add "grapes" to the end of a list using .append().
list.append("grapes")
print(list)
# 3.Insert "kiwi" at position 2 using .insert().
list.insert(2,"kiwi")
print(list)
# 4.Remove "banana" from a list using .remove().
list.remove("banana")
print(list)
# 5.Print the total number of items in a list using len().
print("fruits",len(list))

#Looping and Conditions
# 1.Create a list of 5 numbers.
#Use a loop to print only the even numbers.
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i%2==0:
       print(i)
# 2.Find the maximum number in a list using a loop (without max()).
max=list[0]
for num in list:
    if num>max:
        max=num
print(max)
# 3.Create a list of names.
#Print names that start with 'A'.
names=["anu","abisha","abirami"]
print("the names starts with a is:")
for char in names:
    if char.startswith("a"):
       print(char)

# 4.Ask the user to enter 5 numbers and store them in a list.
#Then print the sum of the numbers.
nums = []
for i in range(5):
    n = int(input("Enter number: "))
    nums.append(n)

total = sum(nums)
print("Entered numbers:", nums)
print("Sum is:", total)

# 5.Create a list of numbers.
#Sort it in ascending order using .sort() and print it.
list=[1,2,8,78,63,98]
list.sort()
print(list)

