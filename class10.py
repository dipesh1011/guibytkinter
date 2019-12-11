#dictionary initialization
dict1={'name':'dipesh','age':21,'place':'Nepal'}
print(dict1)

#taking user defined value
dict2={}
name=input("Enter your name:")
age=input("Enter your age:")
place=input("Enter your place:")
dict2['name']=name
dict2['age']=age
dict2['place']=place
print(dict2)

#taking both key and values from user
dict3={}
namek=input("Enter key for first value:")
namev=input("Enter value for key "+namek+":")
agek=input("Enter key for second value:")
agev=input("Enter value for key "+agek+":")
placek=input("Enter key for third value:")
placev=input("Enter value for key "+placek+":")
dict3[namek]=namev
dict3[agek]=agev
dict3[placek]=placev
print(dict3)

#taking items from user using for loop
dict4={}
n=int(input("Enter number of items:"))
for i in range(n):
    key=input("Enter position "+str(i)+"  key:")
    value=input("Enter the value:")
    dict4[key]=value
print(dict4)