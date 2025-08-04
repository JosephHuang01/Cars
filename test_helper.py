from components.common_game_color import CommonGameColor
from components.position import Position

# name, type, position, width, length, bg_color, fg_color
shape_specification = {
    'name': 'Shape',
    'type': 'shape',
    'position': Position(0, 0),
    'width': 50,
    'length': 50,
    'bg_color': CommonGameColor.GRAY,
    'fg_color': CommonGameColor.BLACK
}

print (shape_specification['name'])

arr = [5, 8, 3, 0, 4, 6]
# print(arr)
# i = 1
# j = 5

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def find_smallest(arr):
    #smallest_number = min(arr)
    #return smallest_number
    smallest_number = arr[0]
    for number in arr:
        if number < smallest_number:
            smallest_number = number
    return smallest_number
    #print(number)

def find_largest(arr):
    largest_number = arr[0]
    for number in arr:
        if number > largest_number:
            largest_number = number
    return largest_number

# swap(arr, i, j)
# print(arr)

smallest = find_smallest(arr)
if smallest == 0:
    print('ok')
else:
    print('ko')

largest = find_largest(arr)
if largest == 8:
    print('ok')
else:
    print('ko')

print ("*****************************************************")
arr = [5, 8, 3, 9, 7, 0, 4, 6, 1, 2]
print (arr)
def sort_one_pass(arr):
    # for current_position, number in enumerate(arr):
    #     print (current_position, number)
    length = len(arr) # 6
    index = 0
    while index <= length - 2:
        print(index, index + 1, arr[index], arr[index + 1])
        if arr[index] > arr[index + 1]:
            swap(arr, index, index + 1)
        index += 1
    return arr

def sort(arr):
    length = len(arr)
    index = 0
    while index <= length - 1:
        sort_one_pass(arr)
        index += 1
    return arr

sort_once = sort_one_pass(arr)
print(sort_once)

sorting = sort(arr)
print(sorting)

arr = [5, 8, 3, 9, 7, 0, 4, 6, 1, 2]

def find_largest_number_position(arr):
        largest_number = arr[0]
        largest_number_index = 0
        for index, number in enumerate(arr):
            if number > largest_number:
                largest_number = number
                largest_number_index = index
        return largest_number_index

large = find_largest_number_position(arr)
print(large)

def find_smallest_number_position(arr):
        smallest_number = arr[0]
        smallest_number_index = 0
        for index, number in enumerate(arr):
            if number < smallest_number:
                smallest_number = number
                smallest_number_index = index
        return smallest_number_index

small = find_smallest_number_position(arr)
print(small)