# # stiring 

# a="mynameismasroorali "

# print(a.upper()) # upper jo sare string ko upper case ma kar da ga

# print(a.lower()) # ya sara ko lower kar da ga 

# print(a.find("a")) # ya index batata ha ka word kaha para ha 

# print(a.count("a")) #ya batata ha ka word katni dafa aya ha 

# print(a.capitalize()) # phala word capital kar da ga

# print(a.replace("my name","i am ")) # replace word ko replace kar data ha

# print(a.isupper()) # ya batata ha ka upper case ma ha ya nhi
# print(a.islower()) # ya batata ha ka lower case ma  ha ya nhi


# print(a.isalnum())
# print(a.isalpha())
# print(a.isdigit())


# b="Masroor123"
# print(b.isalnum())
# c="Masroor"
# print(c.isalpha())
# d="123123"
# print(d.isdigit())



# i="   masroor ali zain wasif"

# # print(i.strip()) # strip use hota ha space start or end ma katam karna ka lia 

# print(i.split()) # split use hota string ko list ma convert karna ka lia 


# list=["Masroor","ali"]

# print(" ".join(list)) # this method convert list to string 

# # slicing 


# a="my name is masroor ali "

# print(a[0])
# print(a[0:5]) # positive slicing 
# print(a[-4:-1])# negative slicing 

# print(a[::2])


# list 
# a=[1]
# print(a)

# a.append("Ali") # for one item 
# print(a)

# a.extend(["Zain","Wasif","Masroor ali "]) # for multiple items 

# print(a)


b=[1,2,3]
# b.sort()# sorting 
# b.sort(reverse=True)# reverse sorting 

# b.clear() # puri list katam kar data ha 
# print(b)
 
# b.remove(1) # remove hamesha value hoti ha 
# print(b)

# b.pop(1)
# print(b)

# b.insert(3,"Rana shab") # list ma insert karna ha specific position ma 
# print(b)

# slicing same wa 

# list1=[1,2,33,4,5,1]
# list2=[66,7,8,9,10]

# list1.extend(list2)
# list1.sort()
# print(list1)

# print(list1.count(1))


# tuplee

# a=(1,2,3,4,5,1,7,1) #
# print(a.count(1)) # count karta ha katni dafa aye ha ya value 
# print(a.index(3))# index batata ha ka konsa index pa pari ha value 


# # set 
#  # repetation nhi hoti
# a={1,2,3,4}
# b={5,6,7,8,1}

# a.add(6) # value add karna ka lia
# print(a)
# a.discard(6)# value delete karna ka lia 
# print(a)
# print(a.issubset(b)) # ya batata ha ka subset ha ya nhi
# print(a.issuperset(b)) # ya batata ha ka super set ha ya nhi

# print(a.union(b))
# print(a.intersection(b))



# Dicitionery 

# dict1={
#     "Name":"Masroor",
#     "Class":"BSCS",
#     "Roll number":35
# }
# print(dict1.keys())
# print(dict1.items())

# print(dict1.values())
# dict1.update({"Name":"Ali"}) # value update ka lia
# print(dict1)
# dict1.pop("Roll number") # delete ka lia
# print(dict1)
# a=dict1.copy()# copy dictionery ka lia
# print(a)

# dict1["mil"]=3555 # add new value
# print(dict1)
# dict1["Mid term"]="Next year"
# print(dict1)


# nested dictioney

# dict1={
#     "name":"ali",
#     "class":"BS",
#     "Subject":{
#         "Math":10,
#         "Englis":20
#     }
# }
# print(dict1["name"])
# print(dict1["Subject"])
