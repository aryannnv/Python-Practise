from curses.ascii import isalnum


str="aryan is champion"
st="Aryan is the Best"
print(len(str))
print(str[::-1] )
print(str.isalpha())
print(str.isalnum())
print(str.endswith("io"))
print(str.count("a"))
print(str.capitalize())
print(str.find("is")) 
print(str.upper())
print(st.lower())
print(str.replace("is","are"))