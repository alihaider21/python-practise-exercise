arr = [
    [1,2,3],
    [4,5,6],
    [9,8,9]]

length = len(arr)
dg_1 = 0
dg_2 = 0

for i in range(0,length):
    dg_1 += arr[i][i]
    dg_2 += arr[i][length-i-1]


print("The Difference: ",abs(dg_1- dg_2))
