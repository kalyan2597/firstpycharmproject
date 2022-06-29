def sum_Elements_List(a):
    return sum(a)


x = input("Enter length of list : ")
x = int(x)
y = []
for i in range(x):
    b = input()
    y.append(int(b))
print("Sum of numbers in list is {}".format(sum_Elements_List(y)))
