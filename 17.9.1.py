sequence_string = input("Enter a sequence of numbers separated by a space: ")
element_string = input("Enter any number: ")

# validate input
sequence_string_list = sequence_string.split(" ")
sequence_float_list = []

for i in sequence_string_list:
  try:
    sequence_float_list.append(float(i))
  except ValueError:
    print("Invalid value", i)
    exit("Bad sequence string")

try:
  element_float = float(element_string)
except ValueError:
  print("Invalid value", element_string)
  exit("Bad search number")

# add element to the list
sequence_float_list.append(element_float)

# sort sequence
sequence_float_list.sort(key=float)

# find element
def binary_search(array, element, left, right):
    if left > right:  
        return False 

    middle = (right + left) // 2 
    if array[middle] == element:  
        return middle  
    elif element < array[middle]:  
        return binary_search(array, element, left, middle - 1)
    else:  
        return binary_search(array, element, middle + 1, right)

element_index = binary_search(sequence_float_list, element_float, 0, len(sequence_float_list) - 1)

if element_index > 0 and sequence_float_list[element_index] > sequence_float_list[element_index - 1] and element_index < len(sequence_float_list) - 1 and sequence_float_list[element_index] <= sequence_float_list[element_index + 1]:
  print("Index:", element_index - 1)
else:
  print("Not found")
print(sequence_float_list)