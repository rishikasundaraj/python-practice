#method1
my_list={"apple":6,"banana":7,"orange":8}
for key in my_list:
    print(key)

#method2
My_list={"maths":49,"Evs":48,"designing":40}
for value in My_list.values():
    print(value)

#method3
my_dict={"mom":40,"dad":50,"brother":25}
for  (key,value) in enumerate(my_dict.items()):
    print(f"{key}{value}")

   #method3
my_dict = {'apple': 3, 'banana': 2, 'orange': 2}
items = list(my_dict.items())

i = 0
while i < len(items):
    key, value = items[i]
    print(f"{key} -> {value}")
    i += 1
 