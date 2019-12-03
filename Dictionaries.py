import statistics as stat
login ={'Admin':'Password' , 'Varad':'vrp12345'}



def main():
  print("""Select Action
                    [1]-Enter Grade
                    [2]-Remove Students
                    [3]-Student Avg Grades
                    [4]-Exit
                    """)
  action=input('Select Action')

  if action=='1':
    print('1')
  elif action=='2':
    print('2')
  elif action=='3':
    print('3')
  elif action=='4':
    exit()
  else:
    print('No Valid Action Taken')

usrnm=input('Username')
passw=input('Password')
if usrnm in login:
    if login[usrnm]==passw:
      print('Welcome',usrnm)
      while True:
        main()
        
