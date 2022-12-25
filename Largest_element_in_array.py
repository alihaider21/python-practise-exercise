def max_elem(lst):
    max = 0
    for i in range(len(lst)):
        if max < lst[i]:
            max = lst[i]
    return max

List = [1,4,2,6,2,9,11,0,3]

print(max_elem(List))