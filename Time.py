import time
now=time.time()
i=0
while(i<5):
    print("Aryan is the Champion")
    time.sleep(2)
    i=i+1
print("The loop ran in",time.time()-now,"secs")
now2=time.time()
for i in range(5):
    print("Aryan is the Champion")
print("The loop ran in",time.time()-now2,"secs")

local=time.asctime(time.localtime(time.time()))
print(local)