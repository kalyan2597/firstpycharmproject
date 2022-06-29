def sum_Elements_List(a):
    return sum(a)


x = input("Enter length of list : ")
x = int(x)
y = []
for i in range(x):
    b = input()
    y.append(int(b))
print("Sum of numbers in list is {}".format(sum_Elements_List(y)))

def isPrime(d):
    if d==1:
        return False
    for i in range(2,d):
        if d%i==0:
            return False
    else:
        return True

print(list(filter(isPrime,y)))


