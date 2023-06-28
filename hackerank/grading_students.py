# def students(grades):
#     return [(i+5-(i%5)) if (i%5>2 and i>=38) else i for i in grades]

grades = [73,67,38,33]
lst = []
for i in grades:
    if i%5>2 and i>=38:
        lst.append(i+5-(i%5))
    else:
        lst.append(i)

print(lst)