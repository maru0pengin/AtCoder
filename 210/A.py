N, A, X, Y = map(int, input().split())

sub = N - A

if sub <= 0:
  print(X*N)
else :
  print(X*A + sub*Y)
