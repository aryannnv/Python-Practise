def fun(normal,*lul,**lmao):
    print(normal)
    for i in lul:
        print(i)
    for item,value in lmao.items():
        print(f"\nThe Rhyming Words are {item} : {value}")
l=["Aryan","Ved","Rohan","Aman","Adi"]
lmlul={"Champu":"Pampu","Dimpu":"Pimpu","Popu":"Lopu","Chinku":"Pinku"}
n="I am Champion"
fun(n,*l,**lmlul)