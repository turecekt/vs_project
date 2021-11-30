def minimax(cislo):
  minimum = cislo[0]
  maximum = cislo[0]
  for num in cislo:
    if num < minimum:
        minimum = num 
    if num > maximum:
        maximum = num
  return minimum,maximum
print(minimax([1,2,3,-1]))