s = float(input())
X = int(s)
Y = round((s - int(s))*10)
if 0 <= Y and Y<=2:
  print(X,'-',sep='')
if 3 <= Y and Y<=6:
  print(X)
if 7 <= Y and Y<=9:
  print(X,'+',sep='')


