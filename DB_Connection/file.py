from numpy.random import randint

f=open("events.txt","w+")
for i in range(1,100000):
    r=str(randint(low=10,high=30))
    f.write(r)

cont=f.read()
print(cont)

f.close()

