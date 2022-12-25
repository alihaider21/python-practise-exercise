# find a number in list

def search(target,my_list):
    for idx,value in enumerate(my_list):
        if value == target:
            return idx
    return -1

target = 5
my_list = [1,2,3,4,5,6,7,8]

result = search(target,my_list)
if result == -1:
    print('value not found')
else:
    print('the index of value is: ', result)