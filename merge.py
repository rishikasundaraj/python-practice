#method1
lst1=[1,2,3,4,5]
lst2=[6,7,8,9]
merge=lst1+lst2
print(merge)

#method2
lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst1.extend(lst2)
print(lst1)