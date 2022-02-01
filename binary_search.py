def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    mid_point = (first + last) // 2

    if list[mid_point] == target:
      return mid_point
    elif list[mid_point] < target:
      first = mid_point + 1
    else:
      last = mid_point - 1
  
  return None


def verify(result):
  if result is not None:
    print(f'Target found at index: {result}')
  else:
    print('Target not found in list')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 3)
verify(result)