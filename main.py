# 1. write a function that checks if nubmer is even or odd

def is_odd_or_even(number):
  if number % 2 == 0: 
   print('Number is even!')
  else: print('Number is odd!')

number = int(input('Enter number: '))
is_odd_or_even(number)