def findData(array, key):
  for data in array:
    if key == data:
      return True
    
  return False

print(findData([1, 2, 3, 5, 9, 4, 7], 9))