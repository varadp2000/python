class Calci:
  x=0
  y=0
  def __init__(self, a, b):
    self.x=a
    self.y=b
  def Add(self):
    return (self.x + self.y)
  def Sub(self):
    return (self.x - self.y)
  def Multi(self):
    return (self.x * self.y)
  def Div(self):
    return (self.x / self.y)



d=0
while(d != 5):
  a=int(input("Enter 1 Number"))
  b=int(input("Enter 2 Number"))
  c=Calci(a,b)
  d=int(input())
  if(d==1):
    print(c.Add())
  elif(d==2):
    print(c.Sub())
  elif(d==3):
    print(c.Multi())
  elif(d==4):
    print(c.Div())
  else:
    print("Enter COrrect Choice")
