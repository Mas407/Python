isinstance

x=10
print(isinstance(x,int))  # ya batata ha ka data type ya ha ya nahi


union type

large project ma use hota ha 

a:int | str       #ik he  variable ma different data store kar satka han 

a=input("Enter the value ")
print(a)


user input un limited 
value=input("Enter the value ").split()

value=list(map(int,input("Enter the value ").split()))

# .split() ya use hota ha data ko list  ma convert karna ka lia

# map is lia use hota ha ka har data ko ik he data type ma convert kar data ha 


print(value)
print(type(value[0]))
print(type(value[1]))
print(type(value[2]))


f string 

name:str="Masroor"  # this is advanced way to write a program 
print(name)
'''

name:str="Masroor"
number:int=1001

this is the advanced way to show value using f string 

print(f"My name is {name} and my roll number is {number}")



# list 
--> in list we can change values we can also store different type of data
--> list is mutable (mutable means change ho sakta ha )
--> list is like an array but list can store any type of data
syntax: list=[1,2,3,4,5]

# tupe 
--> immutable data hota ha means no change 
syntax: a=(1,2,3,4,5)

#set
-->unique data 
syntax:
a={1,2,3,4}

#dictionery

-->keywords || values
syntax:
dict={
"name":"Masroor",
"Number":1001,
"subject":{
    "Math":1,
    "English"=2
}
}





''' 






