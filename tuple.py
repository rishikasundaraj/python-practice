 #Basic Tuple Handling
#Create a tuple of 5 fruits.
#Print the first and last fruit.
fruits = ("apple", "banana", "mango", "orange", "kiwi")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

#Use .count() to count how many times "Delhi" appears in the tuple.
places = ("Delhi", "Mumbai", "Delhi", "Kolkata", "Delhi")
print("Delhi appears:", places.count("Delhi"), "times")

#Use .index() to find the position of "Mumbai" in the tuple.
print(places.index("Mumbai"))
#Loop through a tuple and print each item in uppercase.
for place in places:
    print(place.upper())