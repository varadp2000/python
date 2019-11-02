class Diary:
  def WritetoDiary():
    diaryDate=input('Enter Date')
    diaryText=input('What Special Today?')
    diaryFile=open('diary.txt','a')
    diaryFile.write(diaryDate+'\n'+diaryText+'\n')
    diaryFile.close()


  def ReadDiary():
    diaryFile=open('diary.txt','r').read()
    print(diaryFile)

while (1):
  x=int(input('What do you Want to do in Diary?\n  1.Write 2,Read 3.Exit'))
  if(x==1):
    Diary.WritetoDiary()
    
  if(x==2):
    Diary.ReadDiary()
    
  if(x==3):
    break;

