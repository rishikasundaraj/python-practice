my_list=["apple","banana","orange","apple","banana","orange","apple"]
frequency_dict={}
for item in my_list:
    if item in frequency_dict:
        frequency_dict[item]+=1
    else:
        frequency_dict[item]=1
print(frequency_dict)    
