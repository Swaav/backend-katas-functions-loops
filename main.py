def add(x,y):
  
  return x + y



print(add(5,6))

def multiply(x,y):
    brawl = 0
    for i in range(y):
        brawl = add(x,brawl)

    return brawl


print(multiply(9,9))

def power(x,n):
  bob = 1 
  for i in range(n):
      bob = multiply(x,bob)
  return bob

print(power(3,3))

def factorial(x):
    bugar=1
    for i in range(x,0,-1):
        
        bugar = multiply(i,bugar)
    return bugar



print(factorial(4))


def fibonacci(n):
  forest = 0 
  forestWhitaker = 1
  if n == 0:
      return forest
  elif n == 1:
      return forestWhitaker
  else:
      for i in range(2,n):
          c = add(forest,forestWhitaker)
          forest = forestWhitaker
          forestWhitaker = c
  return forestWhitaker


print(fibonacci(8))