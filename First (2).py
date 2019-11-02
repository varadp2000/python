def fact(z):
  fact=1
  for i in range(1,z):
    fact=i*fact
    return fact
while(1):
  a=int(input("Enter 1st No"))
  b=int(input("Enter 2nd No"))
  print("1 Addition")
  print("2 Subtraction")
  print("3 Multiplication")
  print("4 Division")
  print("5 Power")
  print("6 Exit")
  print("Select Operation")
  c=int(input())
  if(c==1):
    r=a+b
  if(c==2):
    r=a-b
  if(c==3):
    r=a*b
  if(c==4):
    r=a/b
  if(c==5):
    r=a**b
  if(c==6):
    break;
  if(c==7):
    r=fact(a)
  print(r)



