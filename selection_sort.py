#sorting using selection_sort algo
def sorting(arry,size):
    for step in range(size):
        min_index = step

        for i in range(step + 1, size):
            if arry[i] < arry[min_index]:
                min_index = i
        arry[step], arry[min_index] = arry[min_index] , arry[step]

data = [10,4,8,7,1,2]
size = len(data)
sorting(data, size)
print('Sorted Array in Ascending Order:')
print(data)