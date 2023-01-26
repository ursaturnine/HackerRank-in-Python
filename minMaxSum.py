"""Given five positive integers, find the minimum and maximum values that can 
be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers. """

# sort the list
# iterate through list backwards excluding final index to get max_value
def miniMaxSum(arr):
    arr.sort()
    
    min_value = sum(arr[:4])
    max_value = 0
    for num in arr[:-5:-1]:
        max_value += num
    
    print(f'{min_value} {max_value}')