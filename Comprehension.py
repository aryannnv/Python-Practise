# list=[a for a in range(50) if a%5==0]
# print(list)
# dict={b:f"Item {b}" for b in range(5)}
# dict={value:key for key,value in dict.items()} # To reverse the elements of the dict
# print(dict)
size=int(input("Please enter the size of the list: "))
istring=input("Enter the list elements with space: ")
list=istring.split() 
op=int(input("Which type of comprehension do you want: 1.List 2.Dictionary 3.Set: "))
if op==1:
    ls=[i for i in list]
    print(ls)
    print(type(ls))
elif op==2:
    dict={f'item {i}':i for i in list}
    print(dict)
    print(type(dict))
elif op==3:
    se=(i for i in list)
    print(se)
    print(type(se))
