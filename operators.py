#Topic 4: Operators
# 1.Show the result of: 5 + 3, 10 - 2, 4 * 3
print("addition",5+3)
print("subraction",10-2)
print("multiplication",4*3)
# 2.Take two numbers and show +, -, *, /, //, %
a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 3.Ask for base and height, then compute triangle area: 0.5 * base * height
base=int(input("enter the base value"))
height=int(input("enter the height value"))
area=0.5*base*height
print(area)
# 4.Ask for principal, rate, time. Calculate simple interest: (P×R×T)/100
principal=int(input("enter the number"))
ratio=int(input("enter the number"))
time=int(input("enter the number"))
simple_intrest=((principal*ratio*time)/100)
print(simple_intrest)
# 5.Ask for marks in 3 subjects. Print total and average.
maths=int(input("enter the maths mark"))
english=int(input("enter the english mark"))
social=int(input("enter the social mark"))
total=maths+english+social
average=(total/3)
print(total,average)
# 6.Ask for age and check if the person is an adult (age >= 18).
age=int(input("enter the number"))
if age>=18:
    print("adult")
else:
    print("child")
# 7.Use input to calculate: area of circle 3.14 * r * r
radius=int(input("enter the radius"))
area=3.14*radius*radius
print(area)
# 8.Ask for number and print if even (% 2 == 0) or odd.
n=int(input("enter the number"))
if n%2==0:
    print("even")
else:
    print("odd")
# 9.Ask for total marks and obtained marks. Show percentage.
total = float(input("Enter total marks: "))      
obtained = float(input("Enter obtained marks: ")) 
percentage = (obtained / total) * 100
print("Percentage:", percentage, "%")

# 10.Ask user for temperature in Celsius. Convert to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: ")) 
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
