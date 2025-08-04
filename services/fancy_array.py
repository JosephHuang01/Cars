class FancyArray():
    def __init__(self, arr):
        self.arr = arr
    
    def is_less_than(self, a, b):
        return a < b
    
    def is_greater_than(self, a, b):
        return a > b

    def find_magic_number(self, is_magic_number):
        magic_number = 0
        for number in self.arr:
            if (is_magic_number(number)):
                magic_number = number
                break
        return magic_number

    def find_smallest_number(self):
        smallest_number = self.arr[0]
        for number in self.arr:
            if self.is_less_than(number, smallest_number):
                smallest_number = number
        return smallest_number
    
    def find_smallest_number_and_position(self):
        smallest_number = self.arr[0]
        smallest_index = 0
        for index, number in enumerate(self.arr):
            if self.is_less_than(number, smallest_number):
                smallest_index = index
                smallest_number = number
        return smallest_index, smallest_number
    
    def find_largest_number(self):
        largest_number = self.arr[0]
        for number in self.arr:
            if self.is_greater_than(number, largest_number):
                largest_number = number
        return largest_number
    
    def find_largest_number_and_position(self):
        largest_number = self.arr[0]
        largest_index = 0
        for index, number in enumerate(self.arr):
            if self.is_greater_than(number, largest_number):
                largest_index = index
                largest_number = number
        return largest_index, largest_number
    
    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def sort_one_pass_asc(self):
        length = len(self.arr)
        index = 0
        while index <= length - 2:
            #print(index, index + 1, arr[index], arr[index + 1])
            if self.is_greater_than(self.arr[index], self.arr[index + 1]):
                self.swap(index, index + 1)
            index += 1
        return self.arr
    
    def sort_one_pass_desc(self):
        length = len(self.arr)
        index = 0
        while index <= length - 2:
            if self.is_less_than(self.arr[index], self.arr[index + 1]):
                self.swap(index, index + 1)
            index += 1
        return self.arr
    
    def sort_asc(self):
        length = len(self.arr)
        index = 0
        while index <= length - 2:
            self.sort_one_pass_asc()
            index += 1
        return self.arr
    
    def sort_desc(self):
        length = len(self.arr)
        index = 0
        while index <= length - 2:
            self.sort_one_pass_desc()
            index += 1
        return self.arr