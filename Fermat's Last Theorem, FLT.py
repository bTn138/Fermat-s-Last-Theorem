
def perma(d):
  for a in range(2,101):
      for b in range(2,101):
          for c in range(b+1,101):
                  if a**d==(b**d+c**d):
                      print("{},{},{}".format(a,b,c))
                  if a**d<(b**d+c**d):     
                    break    
  print('더는없다')          
for d in range(2,101):
  print(d,'제곱일때 a^2+b^2=c^2을 완성하는 수는')
  perma(d)

