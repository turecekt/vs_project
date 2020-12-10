def main():
  """
  Get user input and check if the input is prime number

  Return None
  """

  print_input()
  text = input()

  while not check_number(text):
    text = input()
    pass

def print_input():
  """
  Print sentece to user
  """
  print('Zadejte číslo k zjíštění, zda je číslo prvočíslo')

def check_number(text: str):
  """
  This function is checking, if the input is Integer if is just return number,
  when is not integer, returning False

  Return Boolean|Integer
  """
  try:
    value = int(text)
    return value
  except ValueError:
    print('Zadaný vstup není celé číslo.')
    print_input()
    return False


if __name__ == '__main__':
  main()
