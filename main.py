def multipleSum(num, multiples):
  sum = 0
  for x in range(1, num):
    for i in range(0, len(multiples)):
      if x % multiples[i] == 0 :
        sum += x
        break  
  return sum 


print(multipleSum(1000, [3, 5]))