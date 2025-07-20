#method1
number=[1,2,3,45,56]
min_value=min(number)
max_value=max(number)
print(max_value)
print(min_value)

#method2
numbers=[1,2,3,7,8]
max=numbers[0]
min=numbers[0]
for num in numbers:
    if num>max:
        max=num
    if num<min:
        min=num
print(max)
print(min)    
