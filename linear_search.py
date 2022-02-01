def linear_search(list, target):
  '''
    finds a target value in a list and returns the index if found. Returns None if not found.
  '''

  for i in range(len(list)):
    if list[i] == target:
      return i

  return None


def verify(result):
  if result is not None:
    print(f'Target found at index: {result}')
  else:
    print('Target not found in list')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 8)
verify(result)