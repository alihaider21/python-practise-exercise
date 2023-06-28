from collections import Counter
# take inputs
n_shoes = int(input())
count_shoes = Counter(input().split())
n_customers = int(input())
cust_dict = {}  # initialize empty dict for customers' needs
for n in range(n_customers):
    cust_dict[n] = input().split()
print(cust_dict.values())


