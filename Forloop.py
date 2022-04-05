from re import L


l=[["harry",1],["carry",5],["marry",15],["larry",4],["barry",20]]
# for item,lolly in l:
#     print(item,"and lollypop is",lolly)
dic=dict(l)
for item,lolly in dic.items():
    print(item,"and lollypop is",lolly)

#No. greater than 6
# l=["harry", int, float, "carry", 55, 4, 3, 88, 45, 13, 7]
# for item in l:
#     # if type(item)==int and item>6:
#     if str(item).isnumeric() and item>6:
#         print(item)