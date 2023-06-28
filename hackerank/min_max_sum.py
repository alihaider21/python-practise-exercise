def miniMaxSum(arr):
    # # Write your code here
    # lst = []
    # for i in range(0,len(arr)):
    #     arr_1 = arr.copy()
    #     arr_1.remove(arr_1[i])
    #     var = 0
    #     for i in range(0,len(arr_1)):
    #         var += arr_1[i]
    #     lst.append(var)
    # return min(lst), max(lst)
    m = sum(arr)
    print(m - max(arr) , m - min(arr))
            

arry = [1,2,3,4,5]

print(miniMaxSum(arry))